#written by EJR on 4/10

from PIL import Image
image=Image.open("C:/Users/emmar/Documents/CLPS0950/CS-Project-Final/dog.jpg")
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
box = (1,2,300,300) #coordinates are left,upper,right,lower
cropped_image=image.crop(box)
cropped_image.show()
#cropped_image=cropped_image.resize((400,400)) #HELP HERE
#cropped_image.show()

#Make the new image 1 and a half the width and one and a half the height of the original image
resized_image = cropped_image.resize((round(cropped_image.size[0]*1.5), round(cropped_image.size[1]*1.5)))
resized_image.show()
#save here if desired


#save processed image 
image=save('new_name.png')