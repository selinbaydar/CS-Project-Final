#EJR wrote this code
#EJR spent 30 minutes writing puesdo code on 4/9,

#define a funciton that takes a folder full of images, then loops through each item in the folder 
#for each image, normalize it first? or at least normalize the size so that the scale of what we zoom in on is the same
#zoom in on the center of the image, feed image to alexnet (or other model) and if alexnet can give the correct answer, the  size of the zoomed in image is the output
#if alexnet cannot give the correct answer, zoom out slightly, repeat until alexnet can identify what the image is


#Questions:
#how can we integrate this with other functions we'll write?
import os
my_directory = r'C:\Users\emmar\Documents\CLPS0950\CS-Project-Final' #i want this to be given in the terminal instead..
def crop(my_directory):
    for filename in os.listdir(my_directory):
        if filename.endswith(".jpg")
            print(os.path.join(directory, filename))
        else:
            continue

