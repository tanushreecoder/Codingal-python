class addition:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def resault(self):
        self.num = self.x + self.y + self.z
        print(self.num)

x = int(input("Enter the first number"))
y = int(input("Enter the second number"))
z = int(input("Enter the third number"))

sum = addition(x, y, z)
sum.resault()