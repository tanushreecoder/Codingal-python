#Create a root window that contains a button. And when the user clicks this button, then a new window will open up using the Top Level functionality of Tkinter.

from tkinter import *

root = Tk()

root.geometry("400x300")

root.title("main")

def topwin():
    
    top = Toplevel()
    
    top.geometry("180x100")
    
    top.title("toplevel")
    
    l2 = Label(top, text="This is toplevel window")
    
    l2.pack()

l = Label(root, text="This is root window")

btn = Button(root, text="Click here to open another window", command=topwin)

l.pack()

btn.pack()

root.mainloop()