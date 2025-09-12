#Here is a file attached. You have to perform the following operations of File Handling using Python
file = open('List.txt', 'r')
print(file.read(8))
file.close()
file = open('List.txt', 'a')
file.write("Laylla = Music")
file.close()