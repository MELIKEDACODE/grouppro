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

def round_corners(original_image, percent_of_side):
    """ Rounds the corner of a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with rounded corners, where
    0 < percent_of_side < 1
    is the corner radius as a portion of the shorter dimension of original_image
    """
    #set the radius of the rounded corners
    width, height = original_image.size
    radius = int(percent_of_side * min(width, height)) # radius in pixels
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
    # Draw two rectangles to fill interior with opaqueness
    drawing_layer.polygon([(radius,0),(width-radius,0),
                            (width-radius,height),(radius,height)],
                            fill=(127,0,127,255))
    drawing_layer.polygon([(0,radius),(width,radius),
                            (width,height-radius),(0,height-radius)],
                            fill=(127,0,127,255))

    #Draw four filled circles of opaqueness
    drawing_layer.ellipse((0,0, 2*radius, 2*radius), 
                            fill=(0,127,127,255)) #top left
    drawing_layer.ellipse((width-2*radius, 0, width,2*radius), 
                            fill=(0,127,127,255)) #top right
    drawing_layer.ellipse((0,height-2*radius,  2*radius,height), 
                            fill=(0,127,127,255)) #bottom left
    drawing_layer.ellipse((width-2*radius, height-2*radius, width, height), 
                            fill=(0,127,127,255)) #bottom right
                         
    # Uncomment the following line to show the mask
    # plt.imshow(rounded_mask)
    
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result
    


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
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = os.path.splitext(file_list[n])
    
        new_image = image_list[n].resize((250, 250)) #resize to 250 x250
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)
    directory = os.path.join(directory, 'modified')
    image_list, file_list = get_images(directory)  

    for n in range(len(image_list)):
        filename, filetype = os.path.splitext(file_list[n])
        new_image = round_corners(image_list[n],.50)
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)   #end nevan Import
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
        dep = dep +1
        filename, filetype = os.path.splitext(file_list[n]) #parses filename
        width, height = image_list[n].size
        midx = width /4 #finds x midpoint
        midy = height /4#finds y midpoint
        big = image_list[n]#takes current image
        try:
            small = image_list[n+1]#takes next image
        except IndexError:
                return "done" #passes when images reach end
        big.paste(small, (midx,midy)) #pastes on top
        
        do_filename = os.path.join(new_directory, filename + '.png')
        big.save(do_filename)#saves to cwd

def makecircles():
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = os.path.splitext(file_list[n])
    
        new_image = image_list[n].resize((250, 250)) #resize to 250 x250
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)
    directory = os.path.join(directory, 'modified')
    image_list, file_list = get_images(directory)  

    for n in range(len(image_list)):
        filename, filetype = os.path.splitext(file_list[n])
        new_image = round_corners(image_list[n],.50)
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    
        