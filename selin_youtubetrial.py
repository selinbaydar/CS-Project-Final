#all the imports needed!
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import cv2
#modules for pytorch
import torch
from torch import nn #nn useful for neural networks
from torch import optim #descent optimizers
import torch.nn.functional as F
from torchvision import datasets, transforms, models

#load the data
# need to make sure the input data is resixed to 224x224 pixels
#validation and testing requires to measure the model's performance o data it hasn't seen yet
#for pre trained networks-normalize the means and standard deviations of the images to what the network expects

#create your directories
#define string of path to the local directory
data_dir = 'flowers'
train_dir = data_dir + '/train'
valid_dir = data_dir + '/valid'
test_dir = data_dir + '/test'

#define transforms for the training, validation and testing sets
#series of transformations done on the images to prepare them to the neural netowrk
#we need structure and standardize the pipeline
training_transforms = transforms.Compose([transforms.RandomRotation(30),
transforms.RandomResizedCrop(224),
transforms.RandomHorizontalFlip(),
transforms.ToTensor(),
transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

validation_transforms = transforms.Compose([
   transforms.Resize(256),
   transforms.CenterCrop(224),
   transforms.ToTensor(),
   transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

testing_transforms = transforms.Compose([
     transforms.Resize(256),
   transforms.CenterCrop(224),
   transforms.ToTensor(),
   transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

