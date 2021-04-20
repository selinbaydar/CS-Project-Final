import tkinter as tk
import PIL
from PIL import Image
from tkinter import *

window = tk.Tk()
window.geometry("400x400+400+400")
text=Text(window)
text.insert(INSERT, "Please ID the image. ")
text.insert(END, "select only one option. ")
text.pack()

img_counter = "burger.jpg"
image1 = Image.open(img_counter)
test = ImageTK.PhotoImage(image1)
label1 = tk.Label(top,image=test)
label1.image=test
label1.place(x=400,y=40)

window.mainloop()