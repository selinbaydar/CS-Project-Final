#the foundational element of a Tkinter GUI is a window!
#windows are the containers in which all other GUI elements live
#ant other elements are called widgets and are contained inside of windows

import tkinter as tk

#create a window
window = tk.Tk()

#add a widget

#add text to the window

# greeting = tk.Label(text="Hello, Tkinter") #this is just creating the widget but you also have to add it to your window
# greeting.pack() #lets you add the widget to the window

# window.mainloop() #tells python to run the Tkinter event loop
#This method listens for events siuch as button clicks or keypresses and blocks

#note DIFFERENT WIDGETS
#label- display text on the screen
#button- can contain a text and can perform an action when clicked
#entry- text entry widget allows only a single line of text
#text- text entry widget that allows multiline text entry
#frame- a rectangular region used to GROUP RELATED WIDGETS or provide padding between widgets

#manipulating the label widget- background and text colors
#colors include red, orange, yellow, green, blue and purple!
# label = tk.Label(
#     text = "Hello, Thinkter",
#     foreground = "white", #can also write fg instead
#     background = "black") #can also write bg instead
# label.pack()
# #can also use hexadecimal RGB values from this URL: https://en.wikipedia.org/wiki/Web_colors#Hex_triplet

#can also control width and height of the label
# label = tk.Label(
#     text="Hello, Tkinter",
#     fg="white",
#     bg="black",
#     width=10,
#     height=10 #even though 10x10 it isnt a square bc width and height are measured in text units
# )
# label.pack()
# window.mainloop() #function doesn't work without window.mainloop() command!!
#note- labels don't get input from users for that you need BUTTONS!

#BUTTONS

button = tk.Button(
    text = "Click me!",
    width = 25,
    height = 5,
    bg = "yellow",
    fg = "black"
)
button.pack()
window.mainloop()
