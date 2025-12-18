import random
print("Let's play rock, paper sissors.")
choices = ['Rock', 'Paper', 'Sissors']
x = input("Choose rock paper or sissors: ")
y = random.randint(choices)
if x == y:
    print("Draw")
elif x == 'Sissors' and y == 'Paper':
    print("You win!")
elif x == 'Paper' and y == 'Sissors':
    print("I win!")
elif x == 'Rock' and y == 'Paper':
    print("I win")
elif x == 'Paper' and y == 'Rock':
    print("You win")
elif x == 'Sissors' and y == 'Rock':
    print("I win")
elif x == 'Rock' and y == 'Sissors':
    print("You win")
else:
    print("Run again and input a proper answer")