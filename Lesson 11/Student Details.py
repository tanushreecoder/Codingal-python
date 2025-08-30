#Write a program to create a parent class Person (attributes - fname, lname) with a method printname to display the full name. Create a child class Student (attributes - fname, lname, year). Access the attributes of parent class in child class using super() function. Then, create an object for the child class and call the display method to display the full name. Also, print the graduation year.

class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def printname(self):
        print(self.firstname)
        print(self.lastname)
class Student(Person):
    def __init__(self, firstname, lastname, graduationyear):
        self.graduationyear = graduationyear
        super().__init__(firstname, lastname)
obj = Student("Tanushree", "Saha", 2031)
obj.printname()
print(obj.graduationyear)