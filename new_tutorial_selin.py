# # # #tensors 

# # # #understanding numpy
# # # import numpy as np
# # # import math
# # # #create random input and output data
# # # x = np.linspace(-math.pi, math.pi, 2000)
# # # y = np.sin(x)

# # # #randomly initialize weights
# # # a = np.random.randn()
# # # b = np.random.randn()
# # # c = np.random.randn()
# # # d = np.random.randn()

# # # learning_rate = 1e-6
# # # for t in range(2000):
# # #     #to compute the predicted y
# # #     #write an equation for what you want y to be
# # #     y_pred = a + b * x + c * x ** 2 + d * x ** 3

# # #     #compute and print loss
# # #     loss = np.square(y_pred - y).sum()
# # #     if t%100 == 99:
# # #         print(t, loss)
# # #     # Backprop to compute gradients of a, b, c, d with respect to loss
# # #     grad_y_pred = 2.0 * (y_pred - y)
# # #     grad_a = grad_y_pred.sum()
# # #     grad_b = (grad_y_pred * x).sum()
# # #     grad_c = (grad_y_pred * x ** 2).sum()
# # #     grad_d = (grad_y_pred * x ** 3).sum()

# # #     # Update weights
# # #     a -= learning_rate * grad_a
# # #     b -= learning_rate * grad_b
# # #     c -= learning_rate * grad_c
# # #     d -= learning_rate * grad_d

# # # print(f'Result: y = {a} + {b} x + {c} x^2 + {d} x^3')

# # #understanding Tensors
# # #a tensor is an n-dimensional array, and PyTorch provides many functions for opeerating on these Tensors
# # #the same example above done with tensors!

# # import torch
# # import math

# # dtype = torch.float
# # device = torch.device("cpu")
# # #all of the things below are the same as numpy besides the addition of device and data type
# # # Create random input and output data
# # x = torch.linspace(-math.pi, math.pi, 2000, device=device, dtype=dtype)
# # y = torch.sin(x)

# # # Randomly initialize weights
# # a = torch.randn((), device=device, dtype=dtype)
# # b = torch.randn((), device=device, dtype=dtype)
# # c = torch.randn((), device=device, dtype=dtype)
# # d = torch.randn((), device=device, dtype=dtype)

# # learning_rate = 1e-6
# # for t in range(2000):
# #     # Forward pass: compute predicted y
# #     y_pred = a + b * x + c * x ** 2 + d * x ** 3

# #     # Compute and print loss
# #     loss = (y_pred - y).pow(2).sum().item()
# #     if t % 100 == 99:
# #         print(t, loss)

# #     # Backprop to compute gradients of a, b, c, d with respect to loss
# #     grad_y_pred = 2.0 * (y_pred - y)
# #     grad_a = grad_y_pred.sum()
# #     grad_b = (grad_y_pred * x).sum()
# #     grad_c = (grad_y_pred * x ** 2).sum()
# #     grad_d = (grad_y_pred * x ** 3).sum()

# #     # Update weights using gradient descent
# #     a -= learning_rate * grad_a
# #     b -= learning_rate * grad_b
# #     c -= learning_rate * grad_c
# #     d -= learning_rate * grad_d


# # print(f'Result: y = {a.item()} + {b.item()} x + {c.item()} x^2 + {d.item()} x^3')

# #HOW TO SAVE MODELS
# import torch

# torch.save(model.state_dict(), "model.pth")
# print("Saved Pytorch Model State to model.pth")
# #HOW TO LOAD MODELS!
# model = NeuralNetwork()
# model.load_state_dict(torch.load("model.pth"))

# #TO EVALUATE THE MODEL
# classes = [
#     "T-shirt/top",
#     "Trouser",
#     "Pullover",
#     "Dress",
#     "Coat",
#     "Sandal",
#     "Shirt",
#     "Sneaker",
#     "Bag",
#     "Ankle boot",
# ]
# model.eval()
# x, y = test_data[0][0], test_data[0][1]
# with torch.no_grad():
#     pred = model(x)
#     predicted, actual = classes[pred[0].argmax(0)], classes[y]
#     print(f'Predicted: "{predicted}", Actual: "{actual}"')

#ANOTHER TUTORIAL ON TENSORS
import torch
import numpy as np

#to initialize a teensor

#initialize directly from the data
data = [[1,2], [3,4]]
x_data = torch.tensor(data)

#or
#initialize from a NumPy array
np_array = np.array(data)
x_np = torch.from_numpy(np_array)

#or
#with random or constant values
shape = (2,3,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f"Random Tensor: \n {rand_tensor} \n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor}")


#ATTRIBUTES OF A TENSOR
#shape, datatype and device

tensor = torch.rand(3,4)

print(f"Shape of tensor: {tensor.shape}") #for tensor shape, which is currently [3,4]
print(f"Datatype of tensor: {tensor.dtype}") #for tensor data type
print(f"Device tensor is stored on: {tensor.device}") #for tensor device, which is currently CPU

#OPERATIONS ON TENSORS
#in ordeer to opeerate on tensors, need to switch from the automatic CPU to GPU!
#use the .to function to switch!
#if GPU is avaiable we move it to GPU with 
#if torch.cuda.is_available():
#tensor = tensor.to('cuda')

if torch.cuda.is_available():
  tensor = tensor.to('cuda')

#after switching to GPU, you can do indexing and slicing to the tensor
#examples:
tensor = torch.ones(4, 4)
print('First row: ',tensor[0])
print('First column: ', tensor[:, 0])
print('Last column:', tensor[..., -1])
tensor[:,1] = 0
print(tensor)

#to concataneta tensors use torch.cat
t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(t1)

#to compute element wise product
# 3 different options
# all produces the same output
z1 = tensor * tensor
z2 = tensor.mul(tensor)
z3 = torch.rand_like(tensor)
torch.mul(tensor, tensor, out=z3)



