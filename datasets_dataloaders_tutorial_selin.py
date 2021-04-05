# DATASETS AND DATALOADERS TUTORIAL

#to load a dataset
#using the Fashion-MNSIT database
#Each example comprises a 28×28 grayscale image and an associated label from one of 10 classes.

#4 parameters of a dataset
#root- the path where the train/test data is stored
#train- specifies training or test data
#download=True- downloads the data from the internet if it's not available at root
#transform and target_transform specify thee feature and label transformations

import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda
import matplotlib.pyplot as plt


training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False, # since we aren't training the data this is False
    download=True,
    transform=ToTensor()
)

#Iterating and Visualizing the Dataset

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
#using matplotlib we visualize the data
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
