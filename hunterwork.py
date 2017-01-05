import PIL
import matplotlib.pyplot as plt
import os.path  
#import functions and libraries

def paste(directory = None):
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed 
    image_list, file_list = get_images(directory)#pulls images from list
    for n in range(len(image_list)):
            