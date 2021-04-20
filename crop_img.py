# EJR wrote, debugged and tested this code
# a function that takes in 5 inputs-a photo and 4 inputs specifying the dimensions for cropping, and gives a cropped photo
# find a tensor--> image funciton and vice versa
# need this to be in pytorch...need the input to be a tensor not an image. 
# how to crop a tensor?? 
def crop_me(image,left_box,upper_box,right_box,lower_box):
    
    # resize the image
    image=image.resize((400,400))

    # crop the image
    # create an integer to loop over box sizes.
    box = (left_box,upper_box,right_box,lower_box) #coordinates are left,upper,right,lower
    cropped_image=image.crop(box)
    #cropped_image.show()
    # cropped_image=cropped_image.resize((400,400)) #HELP HERE
    #cropped_image.show()

    # Make the new image 1 and a half the width and one and a half the height of the original image
    resized_image = cropped_image.resize((round(cropped_image.size[0]*2), round(cropped_image.size[1]*2)))
    resized_image=resized_image.resize((400,400)) #why isn't this changing anything??
    #resized_image.show()

    # save processed image, is there any reason to save here?...
    #resized_image=save('new_name.png')

    # these variables will be defined in zoom_game, and change based on if the computer is getting stuff right or not
    return resized_image
#crop_me("C:/Users/emmar/Documents/CLPS0950/CS-Project-Final/jeep.jpg",160,160,240,240)