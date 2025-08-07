x = int(input("Enter your number: "))
for i in range(0, x):
    for y in range(0, i + 1):
        print("*", end = " ")
    print("\n")