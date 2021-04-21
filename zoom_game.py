#EJR wrote, debugged and tested this code
#SB reviewed this code and helped brainstorm changes

# settings CV for EJR: python.pythonPath": "C:\\Users\\emmar\\Anaconda3\\envs\\CLPS0950\\python.exe
#define a funciton that takes a folder full of images, then loops through each item in the folder

#import all required packages, make sure they are previously installed in workspace
import os
import torchvision.models as models
import torch
import matplotlib.pyplot as plt
import numpy as np
from crop_img import crop_me
from PIL import Image
from torchvision import transforms

#define a function that has an input called my_directory
def zoom_me(my_directory):
    #double check that this directory exists
    if os.path.exists(my_directory):
        print('path exists')
    #import ipdb;ipdb.set_trace() #setting a breakpoint
    # loop over each jpg image in directory
    my_files=os.listdir(my_directory)
    # sort files in alphabetical order 
    my_files=sorted(my_files)

    #initialize vectors where the answers to each model will be stored
    alex_sl = []
    squeeze_sl = []
    resnet_sl = []
    vgg_sl=[]
    dense_sl =[]
    img_counter = 0
    for filename in my_files:
        # initialize img_counter to keep track of which image we are at
        if filename.endswith(".jpg"):
            image_counter=os.path.join(my_directory, filename)
            print(image_counter)
        else:
            continue
        #open the answerkey for our ten images
        with open('answer_key.txt') as g:
            answers=[line.strip() for line in g.readlines()]
        #load image
        img = Image.open(image_counter)
        left_box=190
        upper_box=190
        right_box=210
        lower_box=210
        counter=max(left_box,upper_box,right_box,lower_box)
        # now take the image and zoom in on it using a the function crop_me
        crop_level = 1
        while counter < 400: # we don't want the cropped dimensions to exceed the size of the photo, which is normalized to 400x400
            #display message to state crop level and which image we are looking at so that user can follow along with terminal window
            my_msg = 'We are at crop level:'
            my_msg2 = 'of image:'
            my_msg3 = answers[img_counter].split(',')
            crop_msg= str(crop_level)
            print(my_msg+crop_msg+ ' ' +my_msg2+ ' ' + my_msg3[1])
            img_croped = crop_me(img,left_box,upper_box,right_box,lower_box)
            
            # normalize the image
            transform = transforms.Compose([transforms.Resize(256),
                transforms.CenterCrop(224), 
                transforms.ToTensor(), 
                transforms.Normalize(
                    mean=[0.485,0.456,0.406],
                    std=[0.229,0.224,0.225]
                    )])
            img_t = transform(img_croped)

            #visualize transformed image
            #plt.imshow(img_t[0])
            #plt.show()
            #create batches, which will also turn the 3D image into a 4D tensor which the models can process
            batch_t = torch.unsqueeze(img_t,0)
            print(batch_t.shape)

            # now have the model (such as alexnet) evaluate the picture. This is where we would also have a user view it?
            # to do: figure out how to integrate GUI starting at this point in the code
            # to do: plan what we want GUI to look at and when 
                # Geo suggested having the user decide what the image is via a multiple choice question
            
            #load the pre-trained models (5 total)
            alexnet = models.alexnet(pretrained=True)
            squeezenet1_0 = models.squeezenet1_0(pretrained=True)
            resnet18 = models.resnet18(pretrained=True)
            vgg16 = models.vgg16(pretrained=True)
            densenet161 = models.densenet161(pretrained=True)
            #import ipdb;ipdb.set_trace() #setting a breakpoint
            #put model in evaluation mode
            alexnet.eval()
            squeezenet1_0.eval()
            resnet18.eval()
            vgg16.eval()
            densenet161.eval()
            #define outputs 
            out1 = alexnet(batch_t)
            out2 = squeezenet1_0(batch_t)
            out3 = resnet18(batch_t)
            out4 = vgg16(batch_t)
            out5 = densenet161(batch_t)
            print(out1.shape,out2.shape,out3.shape,out4.shape,out5.shape)

            #open textfile that has the classes

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
    
            #print the label that the model decides, and the percentage certainty.
            print(labels[index1[0]],percentage1[index1[0]].item())
            print(labels[index2[0]],percentage2[index2[0]].item())
            print(labels[index3[0]],percentage3[index3[0]].item())
            print(labels[index4[0]],percentage4[index4[0]].item())
            print(labels[index5[0]],percentage5[index5[0]].item())
            #import ipdb;ipdb.set_trace() #setting a breakpoint
            #import ipdb;ipdb.set_trace() #setting a breakpoint
            
            # create a vector with all the answers from all the models
            all_index = [labels[index1[0]], labels[index2[0]], labels[index3[0]], labels[index4[0]], labels[index5[0]]]

            #import ipdb;ipdb.set_trace() #setting a breakpointn
            # img_counter is keeping track of what image we are on, so each row should correspond
            # individual model answer in vector
            alex_sl = alex_sl + [labels[index1[0]]==answers[img_counter]]
            squeeze_sl = squeeze_sl + [labels[index2[0]]==answers[img_counter]]
            resnet_sl = resnet_sl + [labels[index3[0]]==answers[img_counter]]
            vgg_sl = vgg_sl + [labels[index4[0]]==answers[img_counter]]
            dense_sl = dense_sl + [labels[index5[0]]==answers[img_counter]]
            print(alex_sl)
            print(squeeze_sl)
            print(resnet_sl)
            print(vgg_sl)
            print(dense_sl)
            # score list will store True and False to say if model matches answer key or not
            score_list = [model == answers[img_counter] for model in all_index]

            # repeat loop regardless of if answers are all correct or not
            left_box = left_box - 10
            upper_box = upper_box - 10
            right_box = right_box + 10
            lower_box = lower_box + 10
            counter=max(left_box,upper_box,right_box,lower_box)
            crop_level = crop_level+1

        # to do: define output that says current crop and if it was correct for each model. 

        # increment img_counter, which keeps track of which photo and therefore which answer key index we are at
        img_counter = img_counter+1
    #reshape the answer for each model so that each row corresponds to one model 
    
    alex_sl = np.reshape(alex_sl,[10,19])
    squeeze_sl = np.reshape(squeeze_sl,[10,19])
    resnet_sl = np.reshape(resnet_sl,[10,19])
    vgg_sl= np.reshape(vgg_sl,[10,19])
    dense_sl = np.reshape(dense_sl,[10,19])
    print(alex_sl)
    print(squeeze_sl)
    print(resnet_sl)
    print(vgg_sl)
    print(dense_sl)

    return(alex_sl,squeeze_sl,resnet_sl,vgg_sl,dense_sl)
zoom_me('C:/Users/emmar/Documents/CLPS0950/CS-Project-Final')