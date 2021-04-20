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
    T1.set(option1)
    T2.set(option2)
    T3.set(option3)
    T4.set(option4)

    im = Image.open("dog.jpg")#variable
    tim = ImageTk.PhotoImage(im)
    label1.configure(image=tim)
    label1.image = tim


# #track of image num 1-10
image_counter = 0 
# #track zoom level 1-15
zoom_level = 0
# #initialize matrix of user answers all listed as TRUE, which will later be replaced with FALSE if user is wrong
user_ans = np.ones(shape = [10,19])

with open('MC_options.txt') as f: #opens the textfile with the MC option names
    labels=[line.strip() for line in f.readlines()]
    option1 = str(labels[0])
    #option1 = str(labels[image_counter+4])
    #print(option1) - prints out first line 
    option2 = str(labels[1])
    #option2 = str(labels[image_counter+3])
    option3 = str(labels[2])
    #option3 = str(labels[image_counter+2])
    option4 = str(labels[3])
    #option4 = str(labels[image_counter+1])
    #need to make it so labels[x] turns into new one each time image_counter increases 

def check_ans(image_counter):
    #image counter still not working but when it does->
    if ....get() == answer_opt_type[image_counter]:
        #reassigned onvalues for each buttion to 1,2,3,4 -> can then compare to answer_opt_type to see if correct
        #think this works only with radiobutton?
        image_counter = image_counter + 1 #moves image_counter to upload next question
        user_ans[image_counter,zoom_level] = True
    else:
        # change crop size
        user_ans[image_counter,zoom_level] = False

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


#maybe change to Radiobutton- where user can only select one button, loop written in quiz.py on how to implement and change variables
T1 = StringVar()
T2 = StringVar()
T3 = StringVar()
T4 = StringVar()
#T1.set('hello')
C1 = tk.Checkbutton(top, textvariable = T1, variable = var1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10,)
C2 = tk.Checkbutton(top, textvariable = T2, variable = var2, \
                 onvalue = 2, offvalue = 0, height=5, \
                 width = 10)
C3 = tk.Checkbutton(top, textvariable = T3, variable = var3, \
                 onvalue = 3, offvalue = 0, height=5, \
                 width = 10)
C4 = tk.Checkbutton(top, textvariable = T4, variable = var4, \
                 onvalue = 4, offvalue = 0, height=5, \
                 width = 10)
C1.pack()
C2.pack()
C3.pack()
C4.pack()

selectButton = tk.Button(top, text='Submit', command=onSelect)
selectButton.pack(side = tk.LEFT)

top.mainloop()