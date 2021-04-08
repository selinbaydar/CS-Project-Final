import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import pandas as pd
from torchvision import datasets, transforms as T
import torchvision.models as models
alexnet = models.alexnet(pretrained=True)
print(alexnet)
transform = T.Compose([T.Resize(256), T.CenterCrop(224), T.ToTensor(), T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])

#import an image
from PIL import Image
img = Image.open("dog.jpg")
