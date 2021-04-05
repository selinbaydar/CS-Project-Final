# #tensors 

# #understanding numpy
# import numpy as np
# import math
# #create random input and output data
# x = np.linspace(-math.pi, math.pi, 2000)
# y = np.sin(x)

# #randomly initialize weights
# a = np.random.randn()
# b = np.random.randn()
# c = np.random.randn()
# d = np.random.randn()

# learning_rate = 1e-6
# for t in range(2000):
#     #to compute the predicted y
#     #write an equation for what you want y to be
#     y_pred = a + b * x + c * x ** 2 + d * x ** 3

#     #compute and print loss
#     loss = np.square(y_pred - y).sum()
#     if t%100 == 99:
#         print(t, loss)
#     # Backprop to compute gradients of a, b, c, d with respect to loss
#     grad_y_pred = 2.0 * (y_pred - y)
#     grad_a = grad_y_pred.sum()
#     grad_b = (grad_y_pred * x).sum()
#     grad_c = (grad_y_pred * x ** 2).sum()
#     grad_d = (grad_y_pred * x ** 3).sum()

#     # Update weights
#     a -= learning_rate * grad_a
#     b -= learning_rate * grad_b
#     c -= learning_rate * grad_c
#     d -= learning_rate * grad_d

# print(f'Result: y = {a} + {b} x + {c} x^2 + {d} x^3')

#understanding Tensors
#a tensor is an n-dimensional array, and PyTorch provides many functions for opeerating on these Tensors
#the same example above done with tensors!

import torch
import math

dtype = torch.float
device = torch.device("cpu")
#all of the things below are the same as numpy besides the addition of device and data type
# Create random input and output data
x = torch.linspace(-math.pi, math.pi, 2000, device=device, dtype=dtype)
y = torch.sin(x)

# Randomly initialize weights
a = torch.randn((), device=device, dtype=dtype)
b = torch.randn((), device=device, dtype=dtype)
c = torch.randn((), device=device, dtype=dtype)
d = torch.randn((), device=device, dtype=dtype)

learning_rate = 1e-6
for t in range(2000):
    # Forward pass: compute predicted y
    y_pred = a + b * x + c * x ** 2 + d * x ** 3

    # Compute and print loss
    loss = (y_pred - y).pow(2).sum().item()
    if t % 100 == 99:
        print(t, loss)

    # Backprop to compute gradients of a, b, c, d with respect to loss
    grad_y_pred = 2.0 * (y_pred - y)
    grad_a = grad_y_pred.sum()
    grad_b = (grad_y_pred * x).sum()
    grad_c = (grad_y_pred * x ** 2).sum()
    grad_d = (grad_y_pred * x ** 3).sum()

    # Update weights using gradient descent
    a -= learning_rate * grad_a
    b -= learning_rate * grad_b
    c -= learning_rate * grad_c
    d -= learning_rate * grad_d


print(f'Result: y = {a.item()} + {b.item()} x + {c.item()} x^2 + {d.item()} x^3')