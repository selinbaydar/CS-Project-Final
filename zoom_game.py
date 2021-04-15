#EJR wrote this code

#define a funciton that takes a folder full of images, then loops through each item in the folder 
#for each image, normalize it first? or at least normalize the size so that the scale of what we zoom in on is the same
#zoom in on the center of the image, feed image to alexnet (or other model) and if alexnet can give the correct answer, the  size of the zoomed in image is the output
#if alexnet cannot give the correct answer, zoom out slightly, repeat until alexnet can identify what the image is

#import all required packages, make sure they are previously installed in workspace
import os
import torchvision.models as models
import torch
import matplotlib.pyplot as plt
#import tensorflow??
from crop_img import crop_me #comment this out if you want to run without cropping
from PIL import Image
from torchvision import transforms

#define a function that has an input called my_directory
def zoom_game(my_directory):
    #double check that this directory exists
    if os.path.exists(my_directory):
        print('path exists')

    #loop over each jpg image in directory
    for filename in os.listdir(my_directory):
        # initialize an img_counter to keep track of how many times we've gone through this first loop/which image and therefore answer key index we are at
        img_counter = 0
        if filename.endswith(".jpg"):
            image_counter=os.path.join(my_directory, filename)
            print(image_counter)
        else:
            continue
        
        #load image
        img = Image.open(image_counter)
        left_box=190
        upper_box=190
        right_box=210
        lower_box=210
        counter=max(left_box,upper_box,right_box,lower_box)
        # now take the image and zoom in on it using a the function crop_me

        while counter < 400: # we don't want the cropped dimensions to exceed the size of the photo, which is normalized to 400x400
        # to do: make this counter range accurate for limitations of crop_me/how the box dimensions work
            img_croped = crop_me(img,left_box,upper_box,right_box,lower_box)
            
            transform = transforms.Compose([transforms.Resize(256),
                transforms.CenterCrop(224), 
                transforms.ToTensor(), 
                transforms.Normalize(
                    mean=[0.485,0.456,0.406],
                    std=[0.229,0.224,0.225]
                    )])
            img_t = transform(img_croped)

            #visualize transformed image
            plt.imshow(img_t[0])
            plt.show()
            #create batches, now we can stack images because this turns 3D into 4D
            batch_t = torch.unsqueeze(img_t,0)
            print(batch_t.shape)

            #now have the model (such as alexnet) evaluate the picture. This is where we would also have a user view it?
            # to do: figure out how to integrate GUI starting at this point in the code
            # to do: plan what we want GUI to look at and when 
                # Geo suggested having the user decide what the image is via a multiple choice question
            
            #load the pre-trained models 
            # we will evaluate multiple models: 5 total 
            #could we list all of them one by one? and in the end we would only display the outcomes of each?
            # to do: change variables 
            alexnet = models.alexnet(pretrained=True)
            googlenet = models.squeezenet1_0(pretrained=True)
            resnet18 = models.resnet18(pretrained=True)
            shufflenet = models.vgg16(pretrained=True)
            mobilenet_v2 = models.densenet161(pretrained=True)
            import ipdb;ipdb.set_trace() #setting a breakpoint
            #put model in evaluation mode
            alexnet.eval()
            googlenet.eval()
            resnet18.eval()
            shufflenet.eval()
            mobilenet_v2.eval()

            out1 = alexnet(batch_t)
            out2 = googlenet(batch_t)
            out3 = resnet18(batch_t)
            out4 = shufflenet(batch_t)
            out5 = mobilenet_v2(batch_t)
            print(out1.shape,out2.shape,out3.shape,out4.shape,out5.shape)

            #open textfile that has the classes,this will be different for each model, so create another variable
            with open('answer_key.txt') as g:
                answers=[line.strip() for line in g.readlines()]

            with open('imagenet_classes.txt') as f:
                labels=[line.strip() for line in f.readlines()]

            _ , index1 = torch.max(out1,1)
            percentage1 = torch.nn.functional.softmax(out1,dim=1)[0]*100
            _ , index2 = torch.max(out2,1)
            percentage2 = torch.nn.functional.softmax(out2,dim=1)[0]*100
            _ , index3 = torch.max(out3,1)
            percentage3 = torch.nn.functional.softmax(out3,dim=1)[0]*100
            _ , index4 = torch.max(out4,1)
            percentage4 = torch.nn.functional.softmax(out4,dim=1)[0]*100
            _ , index5 = torch.max(out5,1)
            percentage5 = torch.nn.functional.softmax(out5,dim=1)[0]*100
            #how to make this work for multiple sets? because index is built in so we can't make it change each time
            #print the label that the model decides, and the percentage certainty.
            print(labels[index1[0]],percentage1[index1[0]].item())
            print(labels[index2[0]],percentage2[index2[0]].item())
            print(labels[index3[0]],percentage3[index3[0]].item())
            print(labels[index4[0]],percentage4[index4[0]].item())
            print(labels[index5[0]],percentage5[index5[0]].item())
            
            # create a vector with all the answers from all the models
            all_index = [labels[index1[0]], labels[index2[0]], labels[index3[0]], labels[index4[0]], labels[index5[0]]]
            #open the answerkey for our ten images (note: this is asuming that the order in our folder will stay the same and therefore the images will be looped over exaclty as specified in key)
            #with open('answer_key.txt') as g:
            #    answers=[line.strip() for line in g.readlines()]

            #compare with what user inputs, create conditional statements that will decide if we go through the crop loop again
            # score list will store 0 and 1s to say if model matches answer key or not
            score_list = [model == answers[img_counter] for model in all_index]
            # use all function, tells us if every item is true (1)
            if all(score_list) == True:
                break
            else:#if alexnet is not correct, zoom out by changing box sizes with the counter
                left_box = left_box - 10
                upper_box = upper_box - 10
                right_box = right_box + 10
                lower_box = lower_box + 10
                counter=max(left_box,upper_box,right_box,lower_box)

        # to do: define output that says current crop and if it was correct for each model. 

        # increment img_counter, which keeps track of which photo and therefore which answer key index we are at
        img_counter = img_counter+1
                # three outputs: 1. correct yes or no, 2. crop size, 3. reaction time
                # to do: if we have time, extend the results by making graphs etc to display how the user performs in comparision to the computer.
    # to do: add return 
zoom_game('C:\\Users\emmar\Documents\CLPS0950\CS-Project-Final') #find a way to make this accessible to everyone's computer rather than making it local