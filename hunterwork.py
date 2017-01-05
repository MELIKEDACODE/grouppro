import PIL
import matplotlib.pyplot as plt
import os.path  
#import functions and libraries


    
    
def get_images(directory=None):#grabs images into PIL files, from PLTW
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list


def paste(directory = None):
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed 
    image_list, file_list = get_images(directory)#pulls images from list
    width, height = original_image.size
    midx = width /2 #finds x midpoint
    midy = height /2#finds y midpoint
    for n in range(len(image_list)):
        width, height = image_list[n].size
        midx = width /2 #finds x midpoint
        midy = height /2#finds y midpoint
        big = PIL.new(image_list[n])#takes current image
        small = PIL.new(image_list[n+1])#takes next image
        big.paste(small, (midx,midy))