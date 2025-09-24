import random
import string

print("I will make an 8-digit password for you")
a = input("Do you want your password to have letters or numbers? ")

x = random.randint(10000000, 99999999)
y = ''.join(random.choices(string.ascii_lowercase, k=8))

if a.lower() in ['numbers', 'number']:
    print(f"Your password is {x}")
elif a.lower() in ['letters', 'letter']:
    print(f"Your password is {y}")
else:
    print("That is not an option. Try again.")