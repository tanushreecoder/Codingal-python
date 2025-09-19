#Write a Python program to - create a Tkinter window, set title to it, and set its geometry. Then create a Tkinter grid of three rows and three columns, add Labels as widgets and also add padding.

import tkinter as tk   #Importing the library

window = tk.Tk()

for i in range(3):    #Row    i = 0, 1, 2

    for j in range(3):   #Collum      j = 0, 1, 2

        frame = tk.Frame(          #Rectangular containor widget that can hold other widgets

        master=window,     #Frame is placed inside the main window

        relief=tk.RAISED,       #Raised Gives the border a 3D border effect

        borderwidth=1      #This checks the thickness of the bordor

        )

        frame.grid(row=i, column=j, padx=5, pady=5)    #Grid + padding
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")

        label.pack()

window.mainloop()          #Keeps the window running and responsive