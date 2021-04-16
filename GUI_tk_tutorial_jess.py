#jess - tktutorial in depth for GUI 
#generalt code goes like this: - creates box
    #import tkinter 
    #top = tkinter.Tk()
    ##...code
    #top.mainloop()
#importing - note python3.x = tkinter.messagebox

#creaating buttons and new windows
import tkinter
import tkinter.messagebox
top = tkinter.Tk()
#when button pressed opens new window names 'hello python' -> shows folder names 'hello world'
def helloCallBack():
   tkinter.messagebox.showinfo( "Hello Python", "Hello World")
#creates button named hello 
#(parent window, list of options....as key-value)
B = tkinter.Button(top, text ="Hello", command = helloCallBack)
B.pack()
top.mainloop()
