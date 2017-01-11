import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw            
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