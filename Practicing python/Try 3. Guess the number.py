import random

x = random.randint(1, 100)

print("I have chosen a number between 1 and 100.")
while True:
    try:
        y = int(input("Pick your number: "))
        
        if y < 1 or y > 100:
            print("Please pick a number between 1 and 100.")
            continue

        if y == x:
            print("🎉 Great job! You guessed it!")
            break
        elif y > x:
            print("Too high. Try again.")
        else:
            print("Too low. Try again.")
    except ValueError:
        print("Please enter a valid number.")