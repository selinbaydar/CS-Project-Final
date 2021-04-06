#EJR, Tkinter tutorial,
# use callback function to update value passed through label 
import tkinter
def callback(*args):
    print('Value changed')
    label['text'] =entry.get()

root = tkinter.Tk()
var = tkinter.StringVar()
var.trace("w", callback)

entry = tkinter.Entry(root, textvariable=var)
entry.pack()

label = tkinter.Label(root)
label.pack()

root.mainloop()
