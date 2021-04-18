#focus on applying GUI with checkmarks for users - possible inclusion to our GUI as options 
#written by jessica
#debug by selin and jay

# import all required packages
#format: w = Checkbutton ( master, option, ... )
from tkinter import *
from PIL import Image, ImageTk
from torchvision import transforms
import tkinter
# import ipdb;ipdb.set_trace() #setting a breakpoint
#modified tutorial code for this porject 

#initialize window
top = tkinter.Tk()
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
label1 = tkinter.Label(top,image=test)
label1.image = test

# Position image
label1.place(x = 400, y= 40)
# top.mainloop()
# to do:do we want to include the image in the GUI - if so...https://www.activestate.com/resources/quick-reads/how-to-add-images-in-tkinter/


#how many variables/options want to have 
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()

#define visual aspects of it (master, option....)


C1 = Checkbutton(top, text = "option 1", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10,)
C2 = Checkbutton(top, text = "option 2", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10)
C3 = Checkbutton(top, text = "option 3", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10)
C4 = Checkbutton(top, text = "option 4", variable = CheckVar4, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10)
C1.pack()
C2.pack()
C3.pack()
C4.pack()

top.mainloop()