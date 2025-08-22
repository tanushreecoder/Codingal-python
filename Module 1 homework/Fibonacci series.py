x = int(input("How many terms of the Fibonacci series would you like? "))

a, b = 0, 1
count = 0

print("Fibonacci Series:")

if x < 0:
    print("Fibonacci series does not take negative numbers. Only integers")

while count < x:
    print(a, end=" ")
    a, b = b, a + b
    count += 1