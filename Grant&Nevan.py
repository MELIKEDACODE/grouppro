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