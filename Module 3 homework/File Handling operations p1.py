file = open('List.txt', 'w')
file.close()
with open('List.txt', 'r') as file:
    data = file.readlines()
    print("The words in this file are")
    for i in data:
        word = i.split()
        print(word)
file.close()