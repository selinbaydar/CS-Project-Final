#written by EJR on 4/10
# a function that takes in 5 inputs-a photo and 4 inputs specifying the dimensions for cropping, and gives a cropped photo

def crop_me(my_img,left_box,upper_box,right_box,lower_box):
    from PIL import Image
    image=Image.open(my_img)
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
    #cropped_image.show()
    # cropped_image=cropped_image.resize((400,400)) #HELP HERE
    # cropped_image.show()

    # Make the new image 1 and a half the width and one and a half the height of the original image
    resized_image = cropped_image.resize((round(cropped_image.size[0]*1.5), round(cropped_image.size[1]*1.5)))
    resized_image=resized_image.resize((400,400)) #why isn't this changing anything??
    resized_image.show()

    # save processed image, is there any reason to save here?...
    resized_image=save('new_name.png')

    # To DO: figure out which box dimensions to use..how to make sure we zoom in on the middle rather than on the side
    # these variables will be defined in zoom_game, and change based on if the computer is getting stuff right or not
crop_me("C:/Users/emmar/Documents/CLPS0950/CS-Project-Final/jeep.jpg",160,160,240,240)
#EJR notes on testing how to crop on 4/14
# 20,20,100,100 was white
# 120,120,200,200 was zoomed in on center of dog neck
# 150,150,180,180 was zoomed in even more on center of dog neck, maybe good level 2
# 160,160,150,150 got an error "tile cannot extend outside image"
# 160,160,170,170 was super zoomed in, there wouldn't be a reason to be more zoomed in than this, maybe good level 1
# 140,140,190,190 for level 3?
# 130,130,200,200 for level 4?
# 120,120,210,210 for level 5?
# 1,1,400,400 will be max
# 200,200,200,200 is just black...



