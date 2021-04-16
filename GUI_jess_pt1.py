#focus on applying GUI with checkmarks for users - possible inclusion to our GUI as options 
#written by jessica

#format: w = Checkbutton ( master, option, ... )
from tkinter import *

import tkinter

#modified tutorial code for this porject 
#initialize 
top = Tk()
#creates text at the top of GUI, would use to give instructions.
text = Text(top)
text.insert(INSERT, "Please identify the image. ")
text.insert(END, "Select only one option. ")
text.pack()
// TODO # action item - make the text portion smaller when displayed, right now takes up half the window

//TODO # do we want to include the image in the GUI - if so...https://www.activestate.com/resources/quick-reads/how-to-add-images-in-tkinter/


#how many variables/options want to have 
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()

#define visual aspects of it (master, option....)


C1 = Checkbutton(top, text = "option 1", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20,)
C2 = Checkbutton(top, text = "option 2", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C3 = Checkbutton(top, text = "option 3", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C4 = Checkbutton(top, text = "option 4", variable = CheckVar4, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C1.pack()
C2.pack()
C3.pack()
C4.pack()

top.mainloop()