import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import pandas as pd
import matplotlib.pyplot as plt
from torchvision import datasets, transforms as T
import torchvision.models as models
import helper
alexnet = models.alexnet(pretrained=True)
print(alexnet)
transform = T.Compose([T.Resize(256), T.CenterCrop(224), T.ToTensor(), T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])

#import an image
import cv2

dataset = datasets.ImageFolder('dog.jpg', transform=transform)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=32, shuffle=True)
images, labels = next(iter(dataloader))
helper.imshow(images[0], normalize=False)

# Save image in set directory
# Read RGB image




# img = cv2.imread('dog.jpg')
# from PIL import Image
# img = Image.open("dog.jpg")


# # Output img with window name as 'image'
# cv2.imshow('image', img) 

# # Maintain output window utill
# # user presses a key- in this case 0
# cv2.waitKey(0) 

# #cv2.destroyAllWindows() # Destroying present windows on screen

# #pre-process the image and prepare a batch to be passed through the network
# img_t = transform(img)
# batch_t = torch.unsqueeze(img_t, 0)

# #model interference

# #put model into the eval mode!
# alexnet.eval()

# #to do interference:
# out = alexnet(batch_t)
# print(out.shape)

# with open('imagenet_classes.txt') as f:
#     classes = [line.strip() for line in f.readlines()]



