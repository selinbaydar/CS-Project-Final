#EJR wrote this code

#define a funciton that takes a folder full of images, then loops through each item in the folder 
#for each image, normalize it first? or at least normalize the size so that the scale of what we zoom in on is the same
#zoom in on the center of the image, feed image to alexnet (or other model) and if alexnet can give the correct answer, the  size of the zoomed in image is the output
#if alexnet cannot give the correct answer, zoom out slightly, repeat until alexnet can identify what the image is


#Questions:
#how can we integrate this with other functions we'll write?
import os
import torchvision.models as models
import torch
import matplotlib.pyplot as pltf
#from crop_img import FUNCTION NAME HERE

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
        from PIL import Image
        img=Image.open(image_counter)
        
        #transform image by resizing, cropping, etc.
        from torchvision import transforms
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

        ##ADD CODE TO ZOOM IN HERE, OR MAYBE ADD ANOTHER LOOP
        #batch_t=crop_me(batch_t, add input here relevent to box size)
        #use break once someone is correct!! use a for loop for box size
        #remember to define left_box,upper_box,right_box,lower_box in the loop (this feeds into crop_img)

        #now have the model (such as alexnet) evaluate the picture. This is where we would also have a user view it?

        #load the pre-trained model 

        #TO DO: figure out how to do multiple models at the same time
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


        #see what other classes the model thought the image belonged to
        _, indices = torch.sort(out, descending=True)
        print([(labels[idx], percentage[idx].item()) for idx in indices[0][:5]])
zoom_game('C:\\Users\emmar\Documents\CLPS0950\CS-Project-Final')