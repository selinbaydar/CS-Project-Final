#EJR wrote this code

#define a funciton that takes a folder full of images, then loops through each item in the folder 
#for each image, normalize it first? or at least normalize the size so that the scale of what we zoom in on is the same
#zoom in on the center of the image, feed image to alexnet (or other model) and if alexnet can give the correct answer, the  size of the zoomed in image is the output
#if alexnet cannot give the correct answer, zoom out slightly, repeat until alexnet can identify what the image is
#use break once someone is correct!! use a for loop for box size


#import all required packages, make sure they are previously installed in workspace
import os
import torchvision.models as models
import torch
import matplotlib.pyplot as pltf
from crop_img import crop_me #comment this out if you want to run without cropping/test it before we figure out that loop
from PIL import Image
from torchvision import transforms

#define a function that has an input called my_directory
def zoom_game(my_directory):
    #double check that this directory exists
    if os.path.exists(my_directory):
        print('path does exist')

    #loop over each jpg image in directory
    for filename in os.listdir(my_directory):
        if filename.endswith(".jpg"):
            image_counter=os.path.join(my_directory, filename)
            print(os.path.join(my_directory, filename))
        else:
            continue
        
        #load image
        img=Image.open(image_counter)
        
        #transform image by resizing, cropping, etc.
        transform = transforms.Compose([transforms.Resize(256),
            transforms.CenterCrop(224), 
            transforms.ToTensor(), 
            transforms.Normalize(
                mean=[0.485,0.456,0.406],
                std=[0.229,0.224,0.225]
                )])
        img_t = transform(img)
        #visualize transformed image
        plt.imshow(img_t[0])
        plt.show()
        #create batches WHY ARE WE DOING THIS STEP???
        batch_t = torch.unsqueeze(img_t,0)
        print(batch_t.shape)

        # now take the image and zoom in on it using a the function crop_me

        #initialize variables for crop_me loop
        left_box=1
        upper_box=2
        right_box=100
        lower_box=100
        counter=max(left_box,upper_box,right_box,lower_box)
        for counter in range(1,400): # we don't want the cropped dimensions to exceed the size of the photo, which is normalized to 400x400
            batch_t=crop_me(batch_t,left_box,upper_box,right_box,lower_box)

            #now have the model (such as alexnet) evaluate the picture. This is where we would also have a user view it?
            # to do: figure out how to integrate GUI starting at this point in the code
            # to do: plan what we want GUI to look at and when 
                # Geo suggested having the user decide what the image is via a multiple choice question
            
            #load the pre-trained model 

            #TO DO: figure out how to do multiple models at the same time
            #could we list all of them one by one? and in the end we would only display the outcomes of each?
            alexnet = models.alexnet(pretrained=True)
            alexnet.eval() #put model in evaluation mode
            out = alexnet(batch_t) #batch_t will switch with whatever the cropped version is
            print(out.shape)

            #open textfile that has the classes,this will be different for each model, so create another variable
            with open('imagenet_classes.txt') as f:
                labels=[line.strip() for line in f.readlines()]

            _ , index = torch.max(out,1)
            percentage = torch.nn.functional.softmax(out,dim=1)[0]*100

            #print the label that the model decides, and the percentage certainty.
            print(labels[index[0]],percentage[index[0]].item())


            #see what other classes the model thought the image belonged to, this step might not be needed
            _, indices = torch.sort(out, descending=True)
            print([(labels[idx], percentage[idx].item()) for idx in indices[0][:5]])

            #compare with what user inputs, create conditional statements that will decide if we go through the crop loop again
            if labels[index[0]] = answers[index[0]]: #if alexnet can correclty identify object, escape loop
                # to do: create answers! we need a text file that has the answers for 5-10 photos that we are going to play this game with
                # to do: select 10 photos that we want to use to run this game. need to make sure that all 10 can fall under one of the classes of the various models we use
                # to do: decide which other models (besides alexnet) we want to compare
                break
            else: #if alexnet is not correct, zoom out by changing box sizes with the counter
                left_box = left_box + 20
                upper_box = upper_box + 20
                right_box = right_box + 20
                lower_box = lower_box + 20
                counter=max(left_box,upper_box,right_box,lower_box)
                # To do: fix these increments so that they make sense, ie play around and see how much we should increase the box dimensions each time-- we could also just start from the center and zoom out?
                # to do: if we have time, extend the results by making graphs etc to display how the user performs in comparision to the computer.
zoom_game('C:\\Users\emmar\Documents\CLPS0950\CS-Project-Final') #find a way to make this accessible to everyone's computer rather than making it local