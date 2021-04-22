#thought process by JO of using radiobuttons
#deselects radiobutton and displays options for each question - image_counter
from tkinter import *
from PIL import Image, ImageTk
from torchvision import transforms
from tkinter import messagebox as mb
import tkinter as tk 
import numpy as np

def onSelect():

    #print(var1.get())
    #print('HI')
    #var1.set(0)
    image_counter = 0
    #names each checkbutton, will change as GUI loops through
    #right now will show correct options AFTER clicking submit, need to set the first ones?
    opt_selected = IntVar()
    '''im = Image.open("dog.jpg")#variable
    tim = ImageTk.PhotoImage(im)
    label1.configure(image=tim)
    label1.image = tim'''

def display_options():
    val = 0 
    #deselects options
    opt_selected.set(0)
    #loops over the options that need to be displayed for text of Radio button
    for option in MC_option[image_counter]:
        opts[val]['text']=option
        val+=1

#rshows radio buttons, eturns list of radio button used to add options
def radio_button():
    q_list = []
    y_pos = 150
    while len(q_list)<4:
        radio_btn = Radiobutton(top, text='', variable=opt_selected,
        value = len(q_list)+1,font=('arial',14))
        q_list.append(radio_btn)
        radio_btn.place(x=100, y = y_pos)
        y_pos +=40
    return (q_list)

#initialize window
top = tk.Tk()
top.geometry("1000x1000+1000+1000")
text = Text(top)
# to do: maybe change to labels
text.insert(INSERT, "Please identify the image. ")
text.insert(END, "Select only one option. ")
text.pack()

'''image1 = Image.open("burger.jpg")
test = ImageTk.PhotoImage(image1)
label1 = tk.Label(top,image=test)
label1.image = test
label1.place(x = 400, y= 40)'''


selectButton = tk.Button(top, text='Submit', command=onSelect)
selectButton.pack(side = tk.LEFT)

top.mainloop()