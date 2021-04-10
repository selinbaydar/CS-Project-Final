#EJR wrote this code
#EJR spent 30 minutes writing puesdo code on 4/9

#define a funciton that takes a folder full of images, then loops through each item in the folder 
#for each image, normalize it first? or at least normalize the size so that the scale of what we zoom in on is the same
#zoom in on the center of the image, feed image to alexnet (or other model) and if alexnet can give the correct answer, the  size of the zoomed in image is the output
#if alexnet cannot give the correct answer, zoom out slightly, repeat until alexnet can identify what the image is


#Questions:
#how can we integrate this with other functions we'll write?
import os

def crop(my_directory):
    my_directory = 'C:\Users\emmar\Downloads\pretend' #i want this to be given in the terminal instead..
    print pwd
    if os.path.exists(my_directory)
        print('yes')
    for filename in os.listdir(my_directory):
        if filename.endswith(".jpg")
            image_counter=os.path.join(my_directory, filename)
            print(os.path.join(my_directory, filename))
        else:
            continue
        from PIL import Image
        img=Image.open(image_counter)

        from torchvision import transforms
            transform = transforms.Compose([transforms.Resize(256),transforms.CenterCrop(224), transforms.ToTensor(), transforms.Normalize(mean=[0.485,0.456,0.406],std=[0.229,0.224,0.225])])
        img_t = transform(img)
        plt.imshow(img_t[0])
        plt.show()
        batch_t = torch.unsqueeze(img_t,0)
        print(batch_t.shape)
        
        alexnet.eval() #put model in evaluation mode
        out = alexnet(batch_t)
        print(out.shape)

        with open('imagenet_classes.txt') as f:
            labels=[line.strip() for line in f.readlines()]

        _ , index = torch.max(out,1)
        percentage = torch.nn.functional.softmax(out,dim=1)[0]*100

        print(labels[index[0]],percentage[index[0]].item())


        #see what other classes the model thought the image belonged to
        _, indices = torch.sort(out, descending=True)
        print([(labels[idx], percentage[idx].item()) for idx in indices[0][:5]])
    return()




