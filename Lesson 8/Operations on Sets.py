myset = {}
print(myset)
myset2 = {1, 2, 2, 3, 3, 4, 4, 4, 4}
print(myset2)
myset2.add(5)
print(myset2)
myset3 = {2, 4, 6, 8}
print("This is set 2", myset2)
print("This is set 3", myset3)
x = myset2.difference(myset3)
print("The difference is", x)
y = myset2.symmetric_difference(myset3)
print("The common parts of set 2 and 3 is", y)