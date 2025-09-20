#Create a Tkinter Application which consists of a root window with a button (with text Scan for the virus). When this button is clicked, it will generate a message box that shows a warning that - Stop! Virus Found.


from tkinter import *

from tkinter import messagebox

root = Tk()

root.geometry("200x200")

def msg():

    messagebox.showwarning("Alert", "Stop! Virus Found.")

button = Button(root, text="Scan for Virus", command=msg)

button.place(x=40, y=80)

root.mainloop()