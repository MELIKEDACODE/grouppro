import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw            
times = 0 
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


#end PLTW functions
def alter_all_images(directory=None):
    
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
    times = 1 #sets counter
    #go through the images and save modified versions

#start nevan import


#end nevan Import
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = os.path.splitext(file_list[n])
        
        # Shrink images
        times += 1 #increments
        new_image = shrink_images(image_list[n], times)
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    
    
def shrink_images(original_image, times):
    width, height = original_image.size
    
    new_image = original_image.resize((width / (1 * times), height / (1 * times))) #resize to smaller
    return new_image

    
    
def paste(directory = None):
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed 
    image_list, file_list = get_images(directory)#pulls images from list
    dep = 0
    
    for n in range(len(image_list)):
        
        filename, filetype = os.path.splitext(file_list[n]) #parses filename
        width, height = image_list[n].size
        widthb, heightb = image_list[0].size
        big = image_list[n]#takes current image
        if dep == 0:#checks for first runtime
            try:
                pwid, phei = image_list[n+1].size
            except IndexError:
                pass
            midx = (width /2)-(pwid /2) #finds x midpoint
            midy = (height /2)-(phei /2)#finds y midpoint
            small = image_list[n+1]#takes next image
            big.paste(small, (midx,midy)) #pastes on top
            do_filename = os.path.join(new_directory, filename + '.png')
            big.save(do_filename)#saves to cwd
            dep = dep+1
        else:
            try:
                pwid, phei = image_list[n+1].size
            except IndexError:
                pass
            midx = (widthb /2)-(pwid /2) #finds x midpoint
            midy = (heightb /2)-(phei /2)#finds y midpoint
            big =PIL.Image.open(do_filename)
            try:
                small = image_list[n+1]
            except IndexError:
                return "done"
            big.paste(small, (midx,midy)) #pastes on top
            do_filename = os.path.join(new_directory, filename + '.png')
            big.save(do_filename)#saves to cwd

def inception():
    alter_all_images()
    os.chdir("modified")
    paste()