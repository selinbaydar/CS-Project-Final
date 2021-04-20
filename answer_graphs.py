# code written, debugged and tested by EJR
# compare the 6 boolean matrixes that correspond to which answers are T/F
#from zoom_game import zoom_me
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd 
#from GUI_jess_pt1 import user_ans
import numpy as np
#import numpy as np
alex_sl = np.random.randint(2, size=[10,19])
#(alex_sl,squeeze_sl,resnet_sl,vgg_sl,dense_sl) = zoom_me(my_directory)
#user_ans = np.ones(shape = [10,19])
# def compare_ans(user_ans,alex_sl,squeeze_sl,resnet_sl,vgg_sl,dense_sl):
#     #extract minimum indices per row
    
# # sum the columns/number of images--> create list
# # sum the columns of alex_sl
alex_c1=np.sum(alex_sl, axis=1)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
names = ['Cheeseburger', 'Labrador_retriever', 'jeep', 'laptop', 'mushroom', 'pillow', 'sunglasses', 'tiger', 'mud_turtle', 'waffle_iron'] 
model_ans = alex_c1
ax.bar(names,model_ans)
plt.title('Alex')
plt.xlabel('images')
plt.ylabel('Number correct per zoom level')
plt.show()