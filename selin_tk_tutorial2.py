#the foundational element of a Tkinter GUI is a window!
#windows are the containers in which all other GUI elements live
#ant other elements are called widgets and are contained inside of windows

import tkinter

#create a window
window = tkinter.Tk()

#add a widget

#add text to the window

greeting = tk.Label(text = "Hello, Thinkter") #this is just creating the widget but you also have to add it to your window
greeting.pack() #lets you add the widget to the window

f1=Frame(w1, height=50, width=50)
f1.pack()

window.mainloop()