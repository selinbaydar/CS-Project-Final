# written by JO (GUI general interface, sorting through options and images) and EJR (zoom/crop, placing GUI interface in correct locations, etc.. )
#debugged and tested by JO 
# import all required packages
from tkinter import *
from PIL import Image, ImageTk
from torchvision import transforms
from tkinter import messagebox as mb
import tkinter as tk 
import numpy as np
from crop_img import crop_me

#sets image size
left_box=170
upper_box=170
right_box=230
lower_box=230


def onSelect():
    #keeps track of how many times submit is pressed
    onSelect.counter += 1
    image_counter = onSelect.counter
    #opens the textfile with the image names to sort through images
    with open('image_names.txt') as f: 
        labels=[line.strip() for line in f.readlines()]
        #will change which image file opens depending on image_counter
        name = str(labels[(image_counter)])
    #sets the image
    my_img = name
    im = Image.open(my_img)#variable
    #cropped image
    im = crop_me(im,left_box,upper_box,right_box,lower_box)
    transform = transforms.Compose([transforms.Resize(240),transforms.CenterCrop(224)])
    im = transform(im)
    tim = ImageTk.PhotoImage(im)
    label1.configure(image=tim)
    label1.image = tim
    #opens the textfile with the MC option names
    with open('MC_options.txt') as f:
        #reads lines
        labels=[line.strip() for line in f.readlines()]
        #define options based off textfile, transforms into strings 
        #button 1 
        option1 = str(labels[(4*image_counter)])
        #button 2
        option2 = str(labels[4*image_counter+1])
        #button 3
        option3 = str(labels[4*image_counter+2])
        #button 4
        option4 = str(labels[4*image_counter+3])
    #names each checkbutton as the option previously defined, will change as GUI loops through
    T1.set(option1)
    T2.set(option2)
    T3.set(option3)
    T4.set(option4)
    #opens answer key 
    with open('GUI_answer.txt') as f:
        #reads file
        labels=[line.strip() for line in f.readlines()]
        #assings int value to text 
        correct_ans = int(labels[image_counter])
        #checks if answer if correct by calling variables (var) assigned to each checkbutton and comparing to answer key
        #each var has unique number associated, why can compare all at once
        if var1.get() == correct_ans or var2.get() == correct_ans or var3.get() == correct_ans or var4.get() == correct_ans:
            print("correct")
        else:
            print('wrong')

    #unselects answers after submit button pressed
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)

#initialization
onSelect.counter = 0 

#initialize window
top = tk.Tk()
top.geometry("1000x1000+1000+1000")
text = Text(top)
#initialize text instructions
text.insert(INSERT, "Please identify the image. ")
text.insert(END, "Select only one option. ")
text.pack()

#initalize the image first seen, cropped version
image1 = Image.open("burger.jpg")
image1 = crop_me(image1,left_box,upper_box,right_box,lower_box)
transform = transforms.Compose([transforms.Resize(240),transforms.CenterCrop(224)])
image1 = transform(image1)
#places images in correct location
test = ImageTk.PhotoImage(image1)
label1 = tk.Label(top,image=test)
label1.image = test
label1.place(x = 400, y= 40)

#how many variables/options want to have 
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()

#variables to assign string to checkbuttons
T1 = StringVar()
T2 = StringVar()
T3 = StringVar()
T4 = StringVar()
#initial options that will show up, before onSelect
T1.set('cheesburger')
T2.set('light_bulb')
T3.set('mouth')
T4.set('garden_salad')

#sets the checkbuttons
C1 = tk.Checkbutton(top, textvariable = T1, variable = var1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20,)
C2 = tk.Checkbutton(top, textvariable = T2, variable = var2, \
                 onvalue = 2, offvalue = 0, height=5, \
                 width = 20)
C3 = tk.Checkbutton(top, textvariable = T3, variable = var3, \
                 onvalue = 3, offvalue = 0, height=5, \
                 width = 20)
C4 = tk.Checkbutton(top, textvariable = T4, variable = var4, \
                 onvalue = 4, offvalue = 0, height=5, \
                 width = 20)
C1.pack()
C2.pack()
C3.pack()
C4.pack()

#sets the select button, calls on onSelect when select is pressed
selectButton = tk.Button(top, text='Submit', command=onSelect)
selectButton.pack(side = tk.LEFT)

#opens GUI
top.mainloop()