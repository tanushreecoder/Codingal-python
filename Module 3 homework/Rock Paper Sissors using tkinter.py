import random
from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("Rock Paper Scissors")
root.geometry("400x500")


win_img = ImageTk.PhotoImage(Image.open("Lesson 17/Youwin.jpg").resize((200, 200)))
lose_img = ImageTk.PhotoImage(Image.open("Lesson 17/Youlose.jpg").resize((200, 200)))
draw_img = ImageTk.PhotoImage(Image.open("Lesson 17/draw.jpg").resize((200, 200)))

choices = ['Rock', 'Paper', 'Scissors']

result_label = Label(root, text="Make your choice!", font=("Arial", 16))
result_label.pack(pady=20)

image_label = Label(root)
image_label.pack(pady=20)

computer_choice_label = Label(root, text="", font=("Arial", 14))
computer_choice_label.pack()

def play(player_choice):
    computer_choice = random.choice(choices)
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        result = "It's a draw!"
        image_label.config(image=draw_img)
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Scissors" and computer_choice == "Paper") or \
         (player_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
        image_label.config(image=win_img)
    else:
        result = "You lose!"
        image_label.config(image=lose_img)

    result_label.config(text=result)

button_frame = Frame(root)
button_frame.pack(pady=20)

rock_btn = Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

root.mainloop()

#This was hard to make and I also needed help so that is why it looks a little advanced