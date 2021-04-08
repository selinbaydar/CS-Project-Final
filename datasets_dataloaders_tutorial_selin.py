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

from matplotlib import pyplot as plt
import cv2
import os
import numpy as np
import torch
import torchvision

#get images of bears and snails

#upload images of bears and snails to the machine
mkdir training_data
mkdir training_data/bear
mkdir training_data/snail
#this is the folder and the training folders of bear and snails
#then upload your images to these folders
def read_image_file(f):
# x = cv2.imread('/content/training_data/bear/0.jpg')
x = cv2.imread(f)
#need to swap blue and red channel
x = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
#also resize the image
x = cv2.resize(x, (224,224))
return x
# plt.imshow(x) if you want to look at the image

#place all images into the machine
bear_imgs = []
for f in os.listdir('training_data/bear'):
    img = read_image_file('training_data/bear' + f)
    bear_imgs.append(img)
snail_imgs = []
for f in os.listdir('training_data/snail'):
    img = read_image_file('training_data/snail' + f)
    snail_imgs.append(img)
print('we have %d bear images and %d snail images' % (len(bear_imgs), len(snail_imgs)))

#then create a pytorch model and run it on the images
 img_model = torchvision.models.resnet18(pretrained=True, progress=True)
#since we want a bear vs snal model- it needs to be 2 classes
img_model.fc = torch.nn.Linear(512,2)
#512 is the number of in features that the model itself has! - we change the number of out features

#to run the model on a single image

x = bear_image[0]
def convert_imgs_to_torch_tensor(imgs):
    x = np.stack(imgs) / 255.0
    x = torch.from_numpy(x).float()
    x = x.permute ([0,3,1,2])
    return x


result = img_model.forward(convert_imgs_to_torch_tensor(bear_imgs))

#if you only do this the results will be horrible since the model isn't trained!

train_images = []
train_labels = []

for img in bear_imgs:
    train_images.append(img)
    train_labels.append(0)
    #for one of them append 0
for img in snail_imgs:
    train_images.append(img)
    train_labels.append(1)
    #for the other one append 1
#need an optimizer to train our model
optimizer = torch.optim.SGD(
    img_model.parameters(),
    lr=0.0001
)

#need a training loop
#compare results with label- via loss
#update model params via optimizer




