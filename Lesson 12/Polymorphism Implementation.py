#Write a program to create two classes Dog and Cat, with the same attributes - (name and age) and methods - (info and make_sound). Create different objects for each class and pass the parameters. Showcase the concept of polymorphism in this program.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I'm a dog, my name is {self.name}. I am {self.age} years old and I like Food")
    def make_sound(self):
        print("I bark")
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I'm a cat, my name is {self.name}. I am {self.age} years old and I like watching outside the window")
    def make_sound(self):
        print("I meow")


objcat = Cat("Munchkin", 5)
objdog = Dog("Daisy", 3)

for i in (objcat, objdog):
    i.info()
    i.make_sound()