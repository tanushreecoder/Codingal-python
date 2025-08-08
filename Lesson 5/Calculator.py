def addition(x, y):
    return x + y
def subtraction(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def division(x, y):
    return x / y

num1 = int(input("Enter the 1st number "))
num2 = int(input("Enter the 2nd number "))

print("The sum is", addition(num1, num2))
print("The subtraction is", subtraction(num1, num2))
print("The product is", multiplication(num1, num2))
print("The Quotient is", division(num1, num2))