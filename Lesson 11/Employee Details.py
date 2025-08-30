#Write a program to create a parent class Person (attributes - name, idnumber) with a method display to display the attributes. Create a child class Employee (attributes - name, idnumber, salary, post). Access the attributes of parent class in child class. Then, create an object for child class and call the display method to display the name and idnumber.

class Person(object):   #Parent class
    def __init__(self, name, idnumber):   #__init__ is the constuctor
        self.name = name
        self.idnumber = idnumber
    def display(self):  
        print(self.name)
        print(self.idnumber)
class Employee(Person):       #Child class
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self, name, idnumber)    #Invoking from the parent class
obj = Employee("James", 842478, 30000, "Junior")  #Creation of an object variable
obj.display()   #Function call