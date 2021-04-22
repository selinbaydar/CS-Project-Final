# EJR wrote, debugged and tested this code
# a function that takes in 5 inputs: a photo and 4 inputs specifying the dimensions for cropping, and gives a cropped photo
def crop_me(image,left_box,upper_box,right_box,lower_box):
    
    # resize the image
    image=image.resize((400,400))

    # crop the image
    box = (left_box,upper_box,right_box,lower_box) #coordinates are left,upper,right,lower
    cropped_image=image.crop(box)

    # Resize cropped image
    resized_image = cropped_image.resize((round(cropped_image.size[0]*2), round(cropped_image.size[1]*2)))
    resized_image=resized_image.resize((400,400))
    resized_image.show()

    return resized_image
#crop_me("C:/Users/emmar/Documents/CLPS0950/CS-Project-Final/jeep.jpg",160,160,240,240)