#Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.

class Computer:    #Creating the class
    def __init__(self):
        self.__maxprice = 600
    def sell(self):
        print("The selling price is", self.__maxprice)
    def setmaxprice(self, price):    
        self.__maxprice = price

obj = Computer()

obj.sell()
obj.setmaxprice(1000)   #Changing the price using the setter function
obj.sell()
