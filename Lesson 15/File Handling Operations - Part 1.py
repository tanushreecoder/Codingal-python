#Here is a file attached. You have to perform the following operations of File Handling using Python

with open('List.txt', 'w') as file:
    file.write("Hello world")
file.close()
with open('List.txt', 'r') as file:
    data = file.readlines()
    print("The words in this file are")
    for i in data:
        word = i.split()
        print(word)
file.close()