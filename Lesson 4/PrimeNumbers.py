x = int(input("What is the number you want to checked if it is a prime number or not? "))
flag = False
if x > 1:
    #Checking for factors
    for i in range(2, x):
        if (x % i) == 0:
            flag = True
            break
if flag == True:
    print(f"The number {x} is not a prime")
else:
    print(f"The number {x} is a prime")
