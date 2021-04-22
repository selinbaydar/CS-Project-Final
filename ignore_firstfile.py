#always include these:
#import torch
#from torch.utils.data import Dataset
#from torchvision import datasets
#from torchvision.transforms import ToTensor, Lambda
#import matplotlib.pyplot as plt


import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda, Compose
import matplotlib.pyplot as plt
#note : y. PyTorch provides two data primitives: torch.utils.data.DataLoader and torch.utils.data.Dataset 
# that allow you to use pre-loaded datasets as well as your own data. 
# Dataset stores the samples and their corresponding labels, 
# and DataLoader wraps an iterable around the Dataset to enable easy access to the samples.

# Download training data from open datasets.
#These are just to download the data from the open datasets!
training_data = datasets.FashionMNIST(
    root="data",
    #root is the path where the train/data is stored
    train=True,
    #specifies training or test dataset
    download=True,
    #download=True downloads the data from the internet if it’s not available at root
    transform=ToTensor(),
    #transform and target_transform specify the feature and label transformations

)
# Download test data from open datasets.
test_data=datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)

batch_size = 64
# Create data loaders
#After downloading the training and test datasets, this code creates data loaders
train_dataloader = DataLoader(training_data, batch_size=batch_size)
test_dataloader = DataLoader(test_data, batch_size=batch_size)

for X, y in test_dataloader:
    print("Shape of X [N, C, H, W]: ", X.shape)
    print("Shape of y: ", y.shape, y.dtype)
    break

#To iterate and visualize the Dataset!
#use matplotlip to visualize

#create a directory
labels_map = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}
figure = plt.figure(figsize=(8, 8))
cols, rows = 3, 3
for i in range(1, cols * rows + 1):
    sample_idx = torch.randint(len(training_data), size=(1,)).item()
    img, label = training_data[sample_idx]
    figure.add_subplot(rows, cols, i)
    plt.title(labels_map[label])
    plt.axis("off")
    plt.imshow(img.squeeze(), cmap="gray")
#plt.show()

#To Create a Custom Dataset for your files
#use pandas

import os
import pandas as pd
from torchvision.io import read_image
class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        #The __init__ function is run once when instantiating the Dataset object. 
        # We initialize the directory containing the images, the annotations file, 
        # and both transforms 
        self.img_labels = pd.read.csv(annotations_file)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        #The __len__ function returns the number of samples in our dataset.
        return len(self.img_labels)

    def __getitem__(self, idx):
        #The __getitem__ function loads and returns a sample from the dataset at the given index idx.
        #Based on the index, it identifies the image’s location on disk, 
        #converts that to a tensor using read_image, 
        #retrieves the corresponding label from the csv data in self.img_labels, 
        #calls the transform functions on them (if applicable), 
        #and returns the tensor image and corresponding label in a Python dict.
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        image = read_image(img_path)
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        sample = {"image": image, "label": label}
        return sample

    
