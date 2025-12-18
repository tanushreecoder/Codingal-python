name = input("What's your name?: ")
mood = input(f"Hello {name}, how are you? (Good/Bad): ")
if mood == 'Good':
    print("I'm glad to hear that!")
elif mood == 'Bad':
    print("I'm sorry to hear that, hope things get better.")
else:
    print("It's okay, sometimes it's hard to put feelings into words.")
print(f"It was nice meeting you {name}. Goodbye!")