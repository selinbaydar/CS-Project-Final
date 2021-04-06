#EJR, tk tutorial. This is a GUI example which gives a window that a user can type text, and keeps track of that text in a listbox
# IMPORTING THE MODULE TKINTER
import tkinter

# THE WINDOW INSTANCE
root = tkinter.Tk()

# WIDTH AND HEIGHT + X AND Y OF THE SCREEN
root.geometry("400x400+400+400")


def pass_value():
    """Passes the value into the label and the listbox"""

    # TAKES THE TEXT IN THE ENTRY (that hase the textvariable = textvar)
    label['text'] = textvar.get()

    # AND INSERT THAT TEXT INTO THE LB
    listbox.insert(tkinter.END, textvar.get())

    # Delete the entry text
    textvar.set("")

textvar = tkinter.StringVar()
def entry():
	"""Creates an entry, a label and a listbox"""
	entry = tkinter.Entry(root, textvariable=textvar)
	entry['font'] = "Arial 28"
	entry.focus()
	entry.pack()
	entry.bind("<Return>", lambda x: pass_value())
    #bind the entry to an action, so that it will appear when the user types enter
	label = tkinter.Label(root)
	label.pack()
	listbox = tkinter.Listbox(root)
	listbox.pack()
	return entry, label, listbox

entry, label, listbox = entry()

root.mainloop()