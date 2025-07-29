x = int(input("Enter your number: "))
if x > 50:
    print("Your number is greater than 50")
    if x % 2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")
else:
    print("Your number is not greater than 50")