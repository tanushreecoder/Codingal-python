print("I am a calculator. So....")
x = input("What do you want me to do? The options are 'add', 'subtract', 'multiply' and 'divide.'")

if x == 'Add':
    y = float(input(f"What is your first number you want me to {x}"))
    z = float(input("Second num?"))
    a = y + z
    print(f"The answer is {a}")
elif x == 'Subtract':
    y = float(input(f"What is your first number you want me to {x}"))
    z = float(input("Second num?"))
    a = y - z
    print(f"The result is {a}")
elif x == 'Multiply':
    y = float(input(f"What is your first number you want me to {x}"))
    z = float(input("Second num?"))
    a = y * z
    print(f"The resault is {a}")
elif x == 'Divide':
    y = float(input(f"What is your first number you want me to {x}"))
    z = float(input("Second num?"))
    a = y / z
    print(f"The resault is {a}")
else:
    print("Try again. That is not an option")