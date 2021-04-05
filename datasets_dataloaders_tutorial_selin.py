# # DATASETS AND DATALOADERS TUTORIAL

# #to load a dataset
# #using the Fashion-MNSIT database
# #Each example comprises a 28×28 grayscale image and an associated label from one of 10 classes.

# #4 parameters of a dataset
# #root- the path where the train/test data is stored
# #train- specifies training or test data
# #download=True- downloads the data from the internet if it's not available at root
# #transform and target_transform specify thee feature and label transformations

# import torch
# from torch.utils.data import Dataset
# from torchvision import datasets
# from torchvision.transforms import ToTensor, Lambda
# import matplotlib.pyplot as plt


# training_data = datasets.FashionMNIST(
#     root="data",
#     train=True,
#     download=True,
#     transform=ToTensor()
# )

# test_data = datasets.FashionMNIST(
#     root="data",
#     train=False, # since we aren't training the data this is False
#     download=True,
#     transform=ToTensor()
# )

# #Iterating and Visualizing the Dataset

# labels_map = {
#     0: "T-Shirt",
#     1: "Trouser",
#     2: "Pullover",
#     3: "Dress",
#     4: "Coat",
#     5: "Sandal",
#     6: "Shirt",
#     7: "Sneaker",
#     8: "Bag",
#     9: "Ankle Boot",
# }
# #using matplotlib we visualize the data
# figure = plt.figure(figsize=(8, 8))
# cols, rows = 3, 3
# for i in range(1, cols * rows + 1):
#     sample_idx = torch.randint(len(training_data), size=(1,)).item()
#     img, label = training_data[sample_idx]
#     figure.add_subplot(rows, cols, i)
#     plt.title(labels_map[label])
#     plt.axis("off")
#     plt.imshow(img.squeeze(), cmap="gray")
# #plt.show()

#A new Tutorial for extending Datasets in Pytorch
import numpy as np
np.set_printoptions(precision=6, suppress=True)
import os
import matplotlib.pyplot as plt

from torchvision.datasets import MNIST
import torch
from torchvision import datasets, transforms

# mnist = datasets.MNIST('/tmp/data',
#                        download=True,  # download if dataset not present on disk
#                        transform=transforms.Compose([
#                            transforms.ToTensor(),
#                            transforms.Normalize((0.1307,), (0.3081,))]))
# data_loader = torch.utils.data.DataLoader(mnist,
#                        batch_size=8,
#                        shuffle=True)
# def show(data_loader):
#     images, foo = next(iter(data_loader))
#     from torchvision.utils import make_grid
#     npimg = make_grid(images, normalize=True, pad_value=.5).numpy()
#     import matplotlib.pyplot as plt
#     fig, ax = plt.subplots(figsize=((13, 5)))
#     import numpy as np
#     ax.imshow(np.transpose(npimg, (1, 2, 0)))
#     plt.setp(ax, xticks=[], yticks=[])

#     return fig, ax
# fig, ax = show(data_loader)
# plt.show()
#puts them in a random order

#in order to crop the images!! in a given dataset example:



mnist = datasets.MNIST('/tmp/data',
                       download=True,  # download if dataset not present on disk
                       transform=transforms.Compose([
                           transforms.CenterCrop(18), #crops the image
                           transforms.ToTensor(),
                           transforms.Normalize((0.1307,), (0.3081,))]))
data_loader = torch.utils.data.DataLoader(mnist,
                       batch_size=8,
                       shuffle=True)

fig, ax = show(data_loader)
plt.show()

#OR TO ZOOM OUT!!! this could be used for the project!- modified to fit our goals!
#zoom out (by cropping by a size bigger than the input size
mnist = datasets.MNIST('/tmp/data',
                       download=True,  # download if dataset not present on disk
                       transform=transforms.Compose([
                           transforms.CenterCrop(128),
                           transforms.ToTensor(),
                           transforms.Normalize((0.1307,), (0.3081,))]))
data_loader = torch.utils.data.DataLoader(mnist,
                       batch_size=8,
                       shuffle=True)

fig, ax = show(data_loader)
plt.show()
#this process could be placed in a for loop so that the data would be zoomed out consistently- starting from the zoomed in version?
