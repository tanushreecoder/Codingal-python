#Write a Python program to remove lines of a file starting with prefix - Coding and store the contents in a new file.

file1 = open('List.txt', 'r')
file2 = open('File2', 'w')
for i in file1.readlines():        #Reading all lines that don't begin with coding
    if not (i.startswith("Coding")):
        print(i)
        file2.write(i)           #Storing only those lines that don't begin with coding
file1.close()
file2.close()