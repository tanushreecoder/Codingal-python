print("So.... Welcome to mathamatic chaos. We'll take 4 nums from you! We will divide the 1st num by the 3rd, subtracts that num by the 2nd num, then multiply the 4th, 3rd and 2nd num and add them together, then we'll divide it with the 1st, 2nd num AND then divide it with 7. Let the chaos begin...")

num1 = int(input("1st num: "))
num2 = int(input("2nd num: "))
num3 = int(input("3rd num: "))
num4 = int(input("4th num: "))
a = num1 / num3
b = a - num2
c = num4 * num3 * num2
d = c + b
e = d / num1
f = e / num2
g = f / 7
print(f"The resault of chaos is...{g}")
