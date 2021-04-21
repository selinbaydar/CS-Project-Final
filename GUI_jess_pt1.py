# written by JO and EJR
# import all required packages
from tkinter import *
from PIL import Image, ImageTk
from torchvision import transforms
from tkinter import messagebox as mb
import tkinter as tk 
import numpy as np


def onSelect():

    #print(var1.get())
    #print('HI')
    var1.set(0)
    #names each checkbutton, will change as GUI loops through
    #right now will show correct options AFTER clicking submit, need to set the first ones?

    #need to make it so labels[x] turns into new one each time image_counter increases 

    my_img = "dog.jpg"
    left_box=190
    upper_box=190
    right_box=210
    lower_box=210
    im = Image.open(my_img)#variable
    tim = ImageTk.PhotoImage(im)
    label1.configure(image=tim)
    label1.image = tim
    #keeps track of how many times submit is pressed
    onSelect.counter +=1
    image_counter = onSelect.counter

    print(image_counter)
    with open('MC_options.txt') as f: #opens the textfile with the MC option names
        labels=[line.strip() for line in f.readlines()]
        #option1 = str(labels[4])
        option1 = str(labels[(4*image_counter)])
        #print(option1) - prints out first line 
        #option2 = str(labels[5])
        option2 = str(labels[4*image_counter+1])
        #option3 = str(labels[6])
        option3 = str(labels[4*image_counter+2])
        #option4 = str(labels[7])
        option4 = str(labels[4*image_counter+3])
    T1.set(option1)
    T2.set(option2)
    T3.set(option3)
    T4.set(option4)
    # if the answer is wrong for a certain image, change variables:             
    #         left_box = left_box - 10
    #         upper_box = upper_box - 10
    #         right_box = right_box + 10
    #         lower_box = lower_box + 10 
    #         zoom_level = zoom_level +1
    # use my_img=crop_me("dog.jpg",left_box,upper_box,right_box,lower_box)
    # user_ans[image_counter,zoom_level] = False
onSelect.counter = 0 
# #track of image num 1-10

# #track zoom level 1-15
zoom_level = 0
# #initialize matrix of user answers all listed as TRUE, which will later be replaced with FALSE if user is wrong
user_ans = np.ones(shape = [10,19])

'''with open('MC_options.txt') as f: #opens the textfile with the MC option names
    labels=[line.strip() for line in f.readlines()]
    #option1 = str(labels[4])
    option1 = str(labels[image_counter+4])
    #print(option1) - prints out first line 
    option2 = str(labels[5])
    #option2 = str(labels[image_counter+3])
    option3 = str(labels[6])
    #option3 = str(labels[image_counter+2])
    option4 = str(labels[7])
    #option4 = str(labels[image_counter+1])
    #need to make it so labels[x] turns into new one each time image_counter increases '''

'''def check_ans(image_counter):
    #image counter still not working but when it does->
    #need something beforehand that goes through T1-T4 and outputs the string only if it was selected: 
    #if var 4==1: 
    #if T4 == answer_opt_type[image_counter]
    #mayble loop though them 
    if ....get() == answer_opt_type[image_counter]:
        #if string of option selected = answer_opt_type of image 
        image_counter = image_counter + 1 #moves image_counter to upload next question
    else:
        # change crop size
'''
# answer_opt_type is a txt file with the correct answers
with open('answer_opt_type.txt') as g:
    answer_opt_type = [line.strip() for line in g.readlines()]



#initialize window
top = tk.Tk()
top.geometry("1000x1000+1000+1000")
text = Text(top)
# to do: maybe change to labels
text.insert(INSERT, "Please identify the image. ")
text.insert(END, "Select only one option. ")
text.pack()

image1 = Image.open("burger.jpg")
test = ImageTk.PhotoImage(image1)
label1 = tk.Label(top,image=test)
label1.image = test
label1.place(x = 400, y= 40)

#how many variables/options want to have 
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()

T1 = StringVar()
T2 = StringVar()
T3 = StringVar()
T4 = StringVar()
#initial options that will show up, before onSelect
T1.set('cheesburger')
T2.set('light_bulb')
T3.set('mouth')
T4.set('garden_salad')


C1 = tk.Checkbutton(top, textvariable = T1, variable = var1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10,)
C2 = tk.Checkbutton(top, textvariable = T2, variable = var2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10)
C3 = tk.Checkbutton(top, textvariable = T3, variable = var3, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10)
C4 = tk.Checkbutton(top, textvariable = T4, variable = var4, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10)
C1.pack()
C2.pack()
C3.pack()
C4.pack()

selectButton = tk.Button(top, text='Submit', command=onSelect)
selectButton.pack(side = tk.LEFT)

top.mainloop()