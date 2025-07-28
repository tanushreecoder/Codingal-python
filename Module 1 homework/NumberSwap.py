x = int(input("Select x: "))
y = int(input("Select y: "))
z = int(input("Select z: "))

print(f"x is {x}, y is {y} and z is {z}")

temp1 = x
x = y
y = z
z = temp1

print(f"After number swapping, z is {z} y is {y} and x is {x}")