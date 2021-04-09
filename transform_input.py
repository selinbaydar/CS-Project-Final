#writen by EJR on 4/8 as part of learning pytorch
from torchvision import transforms
#define a variable transform which is a combination of all the image transformations to be carried out
transform = transforms.Compose([
    #resize image to 256x256 pixels
    transfroms.Resize(256),
    transforms.CenterCrop(224),
    #convert image to pytorch tensor data type
    transforms.ToTensor(),
    #normalize image by setting mean and stdev to specified values
    transforms.Normalize(
    mean=[0.485,0.456,0.406],
    std=[0.229,0.224,0.225]
    )])