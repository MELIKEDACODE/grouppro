import PIL
import matplotlib.pyplot as plt
import os.path  

def get_images(directory=None):
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
''' '''
def inside(times = 5):

    directory = os.getcwd() # Use working directory if unspecified
    image_list, file_list = get_images(directory)
    original_image = image_list[0]
    times = int(times)
    width, height = original_image.size
    for i in range(times):
        width = width / 2
        height = height / 2
        small1 = original_image
        small = small1.resize((width, height))
        og = original_image.paste(small, (0,0) , mask=small)
    filename, filetype = os.path.splitext(file_list[0])
    new_directory = os.path.join(directory, 'modified')
    new_image_filename = os.path.join(new_directory, filename + '.png')
    og.save(new_image_filename)  

''' '''
def resizepasteall(directory=None):
    """ 
    puts images in images
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    #load all the images
    image_list, file_list = get_images(directory)  

    #go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = os.path.splitext(file_list[n])
        
        # Round the corners with radius = 30% of short side
        new_image = inside(image_list[n])
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)  