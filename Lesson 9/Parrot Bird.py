#Write a program to create a class Parrot and perform the following tasks - Create a class variable species Create a __init__ method that has instance variables - name and age Create instances of class Parrot, passing arguments as well Print Class variable by accessing it Print Instance variables as well

class parrot:
    species = "Indian parrot ring neck"
    def __init__(self, name, age):
        self.name = name
        self.age = age
blu = parrot("Blu", 10)
Lemon = parrot("Lemon", 12)

print("Blu is a {}" .format(blu.species))
print("Lemon is a {}" .format(Lemon.species))

print("{} is {} years old" .format(blu.name, blu.age))
print("{} is {} years old" .format(Lemon.name, Lemon.age))
        