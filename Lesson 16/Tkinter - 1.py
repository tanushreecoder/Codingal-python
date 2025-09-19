#Write a Python program to - create a Tkinter window, set title to it, and set its geometry. Then add these widgets to the window - Label, Button, Entry, Frame, and a Text box.

import tkinter as tk
window = tk.Tk()
window.title("Tkinker python")
window.geometry("500x500")
grading = tk.Label(text = "This is the first tkinker :D", fg = "purple", bg = "red")
button = tk.Button(text = "Click me", fg = "red", bg = "purple")
userEntry = tk.Entry(fg = "blue", bg = "light blue", width = 50)
grading.pack()
button.pack()
userEntry.pack()
frame = tk.Frame(master = window, relief = tk.RAISED, width = 5)
frame.pack()
label = tk.Label(text = "Hello world", master = frame) 
textbox = tk.Text(fg = "black", bg = "white", height = 5, width = 30)
label.pack()
textbox.pack()
window.mainloop()