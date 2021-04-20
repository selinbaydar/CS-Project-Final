# import all required packages

from tkinter import *
from PIL import Image, ImageTk
from torchvision import transforms
import tkinter as tk 

def onSelect():
    print(var1.get())
    print('HI')
    var1.set(0)
    T1.set('hehehe')

    im = Image.open("dog.jpg")
    tim = ImageTk.PhotoImage(im)
    label1.configure(image=tim)
    label1.image = tim


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
T1.set('hello')
C1 = tk.Checkbutton(top, textvariable = T1, variable = var1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10,)
C2 = tk.Checkbutton(top, text = "option 2", variable = var2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10)
C3 = tk.Checkbutton(top, text = "option 3", variable = var3, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10)
C4 = tk.Checkbutton(top, text = "option 4", variable = var4, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10)
C1.pack()
C2.pack()
C3.pack()
C4.pack()

selectButton = tk.Button(top, text='Submit', command=onSelect)
selectButton.pack(side = tk.LEFT)

top.mainloop()