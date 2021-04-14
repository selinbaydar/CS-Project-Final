#written by EJR on 4/10
# a function that takes in 5 inputs-a photo and 4 inputs specifying the dimensions for cropping, and gives a cropped photo

def crop_me(my_img,left_box,upper_box,right_box,lower_box):
    from PIL import Image
    image=Image.open(my_directory)
    image.show() #display image

    # The file format of the source file.
    print(image.format)

    # The pixel format used by the image. Typical values are "1", "L", "RGB", or "CMYK."
    print(image.mode)

    # Image size, in pixels. The size is given as a 2-tuple (width, height).
    print(image.size)

    # Colour palette table, if any.
    print(image.palette)

    # resize the image
    image=image.resize((400,400))

    # crop the image
    # create an integer to loop over box sizes.
    box = (left_box,upper_box,right_box,lower_box) #coordinates are left,upper,right,lower
    cropped_image=image.crop(box)
    cropped_image.show()
    # cropped_image=cropped_image.resize((400,400)) #HELP HERE
    # cropped_image.show()

    # Make the new image 1 and a half the width and one and a half the height of the original image
    resized_image = cropped_image.resize((round(cropped_image.size[0]*1.5), round(cropped_image.size[1]*1.5)))
    resized_image=resized_image.resize((400,400)) #why isn't this changing anything??
    resized_image.show()

    # save processed image, is there any reason to save here?...
    #resized_image=save('new_name.png')

    # To DO: figure out which box dimensions to use..how to make sure we zoom in on the middle rather than on the side
    # these variables will be defined in zoom_game, and change based on if the computer is getting stuff right or not
crop_me("C:/Users/emmar/Documents/CLPS0950/CS-Project-Final/dog.jpg",1,2,100,100)