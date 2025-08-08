def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)
x = int(input("Enter a number "))
if x < 0:
    print("Factorial does not exist for negative numbers")
elif x == 0:
    print("The factorial of 0 is 1")
else:
    print(f"The factorial of {x} is", factorial(x))