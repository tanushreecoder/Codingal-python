#Here is a file attached. You have to perform the following operations of File Handling using Python

file = open('List.txt', 'r')
print("Let's read the 1st line")
print(file.readline())
file.close()
file = open('List2.txt', 'r')
print("Reading multiple lines")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
file = open('List.txt', 'r')
print("Looping through the lines")
for i in file:
    print(i)
file.close()