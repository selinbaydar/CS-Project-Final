import torch
import numpy as np
#initializing a tensor
#create tensor directly from data
data = [[1,2],[3,4]]
x_data = torch.tensor(data)
#create tensor from numpy array
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
#create tensor from another tensor
x_ones = torch.ones_like(x_data) #retains the properties of x_data
print(f"Ones Tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float) #overrides the datatype of x_data
print(f"Random Tensor: \n {x_rand} \n")

#create a tensor with random or constant values
#shape is a tuple of tensor dimensions
shape = (2,3,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)
print(f"Random Tensor: \n {rand_tensor} \n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor}")

#Attributes of tensor to descirbe shape, datatype, and device on which they are stored
tensor = torch.rand(3,4)
print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")

#use torch.cat to concatenate a seq of tensors along given dimension
 
 #datasets and Data loaders Tutorial
#two data primitives: torch.utils.data.DataLoader and torch.utils.data.Dataset which preload datasets
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda
import matplotlib.pyplot as plt

training_data = datasets.FashionMNIST(
    root = "data",
    train = True,
    download = True,
    transform=ToTensor()
)

test_data=datasets.FashionMNIST(
    root = "data",
    train = False,
    download = True,
    transform=ToTensor()
)

