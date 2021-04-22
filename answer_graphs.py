# code written, debugged and tested by EJR

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

# # sum the columns/sum across zoom levels
alex_c1=np.sum(alex_sl, axis=0)
squeeze_c1=np.sum(squeeze_sl,axis=0)
resnet_c1=np.sum(resnet_sl,axis=0)
vgg_c1=np.sum(vgg_sl,axis=0)
dense_c1=np.sum(dense_sl,axis=0)
user_c1=np.sum(user_sl,axis=0)

names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11','12','13','14','15','16','17','18','19'] 


plt.suptitle('Number of images correct at each zoom level')
plt.tight_layout(pad=300)
plt.subplot(3,3,1)
plt.bar(names,alex_c1,0.5,color='grey',edgecolor='cyan')
plt.title('Alex')
plt.tick_params(axis='x', which='major', labelsize=0)
plt.tight_layout(pad=300)

plt.subplot(3,3,2)
plt.bar(names,squeeze_c1,0.5,color='grey',edgecolor='cyan')
plt.title('Squeeze')
plt.tick_params(axis='x', which='major', labelsize=0)
plt.tight_layout(pad=300)

plt.subplot(3,3,3)
plt.bar(names,resnet_c1,0.5,color='grey',edgecolor='cyan')
plt.title('Resnet')
plt.tick_params(axis='x', which='major', labelsize=0)
plt.tight_layout(pad=300)

plt.subplot(3,3,4)
plt.bar(names,vgg_c1,0.5,color='grey',edgecolor='cyan')
plt.title('VGG')
plt.tick_params(axis='x', which='major', labelsize=5)
plt.tight_layout(pad=300)

plt.subplot(3,3,5)
plt.bar(names,dense_c1,0.5,color='grey',edgecolor='cyan')
plt.title('Dense')
plt.tick_params(axis='x', which='major', labelsize=5)
plt.tight_layout(pad=300)

plt.subplot(3,3,6)
plt.bar(names,user_c1,0.5,color='cyan', edgecolor='black')
plt.title('YOU! (the user)')
plt.tight_layout(pad=300)

axes = plt.gca()
axes.xaxis.label.set_size(20)
axes.yaxis.label.set_size(20)
plt.tick_params(axis='x', which='major', labelsize=5)
plt.tight_layout(pad=300)

plt.show()

