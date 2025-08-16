import random

print("Pick a number between 1 and 10. I will try to guess it!")

x = list(range(1, 11))
y = False

while not y and x:
    guess = random.choice(x)
    x.remove(guess)

    answer = input(f"Is your number {guess}? (Type 'Yes' or 'No'): ").strip()

    if answer.lower() == "yes":
        print("Great! I guessed it right.")
        y = True

if not y:
    print("I couldn't guess it. Are you sure it was between 1 and 10?")