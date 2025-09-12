print("Do you want to play rock, paper, sissors?")
print("We'll do 5 rounds and the winner will be the person with more points")
import random
1 = "rock"
2 = "sissors"
3 = "paper"
x = random.randint(1, 4)
y = input("What is your first choise?")
print(f"My choise is {x}")
if y == "rock" and x == "paper":
    print("I win!")