# code written, debugged and tested by EJR
# compare the 6 boolean matrixes that correspond to which answers are T/F
#from zoom_game import zoom_me
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd 
#from GUI_jess_pt1 import user_ans
import numpy as np
#import numpy as np

#copied and pasted from zoom_game outputs for the purpose of the presentation (code takes too long to run in 5 minutes)
alex_sl = [False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, False, False, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, 
False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, True, True, True, 
True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
squeeze_sl = [False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, True, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, False, False, False, 
False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, 
False, False, True, False, False, True, False, False, False, False, False, False, False, False, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
resnet_sl = [False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, True, True, False, True, True, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, 
False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, 
False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, True, True, True, False, True, True, True, True, True, True, True, True, True, True, 
True, True, True, True, True, True, True, True]
vgg_sl = [False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, True, True, True, True, 
True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, 
True, True, True, True, True, True, True, True, True, True]
dense_sl = [False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, 
False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, True, True, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, 
False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, True, False, False, False, True, True, True, True, True, False, True, False, False, False, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
alex_sl = np.reshape(alex_sl,[10,19])
squeeze_sl = np.reshape(squeeze_sl,[10,19])
resnet_sl = np.reshape(resnet_sl,[10,19])
vgg_sl= np.reshape(vgg_sl,[10,19])
dense_sl = np.reshape(dense_sl,[10,19])
#this is where we would input the user's performance on the zoom game. It is currently random numbers for the purpose of graphing
user_sl = np.random.randint(2, size=[10,19])

#(alex_sl,squeeze_sl,resnet_sl,vgg_sl,dense_sl) = zoom_me(my_directory)
#user_ans = np.ones(shape = [10,19])
# def compare_ans(user_ans,alex_sl,squeeze_sl,resnet_sl,vgg_sl,dense_sl):
#     #extract minimum indices per row
    
# # sum the columns/number of images--> create list
# # sum the columns of alex_sl
alex_c1=np.sum(alex_sl, axis=0)
squeeze_c1=np.sum(squeeze_sl,axis=0)
resnet_c1=np.sum(resnet_sl,axis=0)
vgg_c1=np.sum(vgg_sl,axis=0)
dense_c1=np.sum(dense_sl,axis=0)
user_c1=np.sum(user_sl,axis=0)

names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11','12','13','14','15','16','17','18','19'] 

plt.subplot(3,3,1)
plt.bar(names,alex_c1,0.5,color='grey',edgecolor='cyan')
plt.xlabel('Crop Level')
plt.title('Alex')

plt.subplot(3,3,2)
plt.bar(names,squeeze_c1,0.5,color='grey',edgecolor='cyan')
plt.xlabel('Crop Level')
plt.title('Squeeze')

plt.subplot(3,3,3)
plt.bar(names,resnet_c1,0.5,color='grey',edgecolor='cyan')
plt.xlabel('Crop Level')
plt.title('Resnet')

plt.subplot(3,3,4)
plt.bar(names,vgg_c1,0.5,color='grey',edgecolor='cyan')
plt.xlabel('Crop Level')
plt.title('VGG')

plt.subplot(3,3,5)
plt.bar(names,dense_c1,0.5,color='grey',edgecolor='cyan')
plt.xlabel('Crop Level')
plt.title('Dense')

plt.subplot(3,3,6)
plt.bar(names,user_c1,0.5,color='cyan', edgecolor='black')
plt.xlabel('Crop Level')
plt.title('YOU! (the user)')

plt.show()

