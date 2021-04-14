# following through with content on this website: https://pytorch.org/vision/stable/models.html#classification
#construct a model with random weights by calling its constructor and leaving everything that says pretrained=true as () instead

#step1: loading pre-trained network using Torchvision
import torchvision.models as models
import torch
import matplotlib.pyplot as plt

#step2: load the pre-trained model 
alexnet = models.alexnet(pretrained=True)
#the purpose of alexnet is to take an image and predict it's class
# QUESTION: what is happening with the directory for the cache?

# some models have diff training and evaluation behavior. switch using model.trian() or model.eval()

# must input images in a normalized way
# using the following transform to normalize:
#normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])
from torchvision import transforms
#define a variable transform which is a combination of all the image transformations to be carried out
#step3: specify image transformations, transform input image
transform = transforms.Compose([
    #resize image to 256x256 pixels
    transforms.Resize(256),
    transforms.CenterCrop(224),
    #convert image to pytorch tensor data type
    transforms.ToTensor(),
    #normalize image by setting mean and stdev to specified values
    transforms.Normalize(
    mean=[0.485,0.456,0.406],
    std=[0.229,0.224,0.225]
    )])

#step4: load input image and pre-process it
from PIL import Image
img=Image.open("C:/Users/emmar/Documents/CLPS0950/CS-Project-Final/dog.jpg")

#pre-process image and prepare a batch to be passed through network
img_t = transform(img)

plt.imshow(img_t[0])
plt.show()

batch_t = torch.unsqueeze(img_t,0)
print(batch_t.shape)

#step5: model inferenc, use pre-trained model to see what model thinks of image
alexnet.eval() #put model in evaluation mode
out = alexnet(img_t)
print(out.shape)

#read and store labels from a text file that has all 1000 labels
with open('imagenet_classes.txt') as f:
    labels=[line.strip() for line in f.readlines()]

#find out index where max score output vector occur, this is the index that will be used to make the prediction
_ , index = torch.max(out,1)
percentage = torch.nn.functional.softmax(out,dim=1)[0]*100

print(labels[index[0]],percentage[index[0]].item())


#see what other classes the model thought the image belonged to
_, indices = torch.sort(out, descending=True)
print([(labels[idx], percentage[idx].item()) for idx in indices[0][:5]])

