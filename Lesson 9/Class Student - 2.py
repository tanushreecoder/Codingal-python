#Write a program to create a class with name Student and perform the following tasks - Create a class variable grade and name Create a function to print a sentence Create a function to print class variables grade and name Create an object of class Student Call the two functions to execute them

class student:  #Defing the class
    grade = 6  #Defining class variables
    name = 'Tanushree'
    def  introduction(self):  #Defining a function
        print(f"Tanushree is a little girl")
    def detailsofself(self):   
        print(f"My name is {self.name}. And my grade is {self.grade}")
ob = student()    #Creating an object of class student
ob.detailsofself()  #Calling functions
ob.introduction()