#focus on applying GUI with checkmarks for users - possible inclusion to our GUI as options 
#written by jessica
#debug by selin and jay

# import all required packages
#format: w = Checkbutton ( master, option, ... )
from tkinter import *
from PIL import Image, ImageTk
from torchvision import transforms
import tkinter as tk
# import ipdb;ipdb.set_trace() #setting a breakpoint
#modified tutorial code for this porject 

#initialize window
top = tk.Tk()

#TO DO: we can add window title
#top.title('')

#define window size
top.geometry("1000x1000+1000+1000")
# what is top??
#creates text at the top of GUI, would use to give instructions.
text = Text(top)
# to do: maybe change to labels
text.insert(INSERT, "Please identify the image. ")
text.insert(END, "Select only one option. ")
text.pack()
# to do: action item - make the text portion smaller when displayed, right now takes up half the window

# Create a photoimage object of the image in the path
image1 = Image.open("burger.jpg")

#transform image so that it is small enough to fit on the display
transform = transforms.Compose([transforms.Resize(240),transforms.CenterCrop(224)])
image1 = transform(image1)

test = ImageTk.PhotoImage(image1)
label1 = tk.Label(top,image=test)
label1.image = test

# Position image
label1.place(x = 400, y= 40)
# top.mainloop()

#to get a general understanding of how to work with checkboxes
#this code changes the text based on the option chosen
#we will want to pre-code which option should be true

# def print_selection():
#     if (var1.get() == 1) & (var2.get() == 0):
#         l.config(text='I love Python ')
#     elif (var1.get() == 0) & (var2.get() == 1):
#         l.config(text='I love C++')
#     elif (var1.get() == 0) & (var2.get() == 0):
#         l.config(text='I do not anything')
#     else:
#         l.config(text='I love both')

#this is from here:https://pythonbasics.org/tkinter-checkbox/

#how many variables/options want to have 
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()

#define visual aspects of it (master, option....)

#need to define the option as a function so that it will change based on the image that is shown
#create an answer key for the options

C1 = tk.Checkbutton(top, text = "option 1", variable = var1, \
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

top.mainloop()

# def retrieve_input():
#     global checkbox_response1
#     global checkbox_response2
#     global checkbox_response3
#     global checkbox_response4
#     checkbox_response1 = C1.get()
#     checkbox_response2 = C2.get()
#     checkbox_response3 = C3.get()
#     checkbox_response4 = C4.get()

#maybe we can add quit function once they get the correct response- but in that case would the matrix size not align?



