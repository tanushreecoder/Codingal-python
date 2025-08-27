print("Hash has a robot, Tom.")

class Robot:
    def __init__(self, name, age, owner, use):
        self.name = name
        self.age = age
        self.owner = owner
        self.use = use

# Create robot instance
Tom = Robot('Tom', '3 years old', 'Hash', 'Good at mathematics')

# Ask user which robot
x = input("Which robot do you want to know about first? ")

if x == "Tom":
    y = input("What do you want to know about Tom? (Name, Age, Owner, Use) ")
    
    if y == "Name":
        print("Tom's name is", Tom.name)
    elif y == "Age":
        print("Tom's age is", Tom.age)
    elif y == "Owner":
        print("Tom's owner is", Tom.owner)
    elif y == "Use":
        print("Tom's use is", Tom.use)
    else:
        print("This is not in his program. Try another keyword.")
else:
    print("That robot is not available for now.")