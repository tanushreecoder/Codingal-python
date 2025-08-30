#Write a program to implement abstraction on animal class (base class). The abstract method will be move that is for displaying what subclasses can do.
from abc import ABC, abstractmethod  #abc is the abtract base class and ABC is the library      #Importing nessicary packages
class animal(ABC):      #Base class
    def move(self):   #Abstract method. It should be implemented by all sub classes.
        pass        
class human(animal):
    def move(self):
        print("I can walk and run")
class dog(animal):
    def move(self):
        print("I can bark and move on 4 legs")
class snake(animal):
    def move(self):
        print("I can move by crawling and I can hiss")
h = human()
h.move()
d = dog()
d.move()
s = snake()
s.move()