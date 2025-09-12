#Write a Python program to copy odd lines from one file to another file. For copying it in a new file, create a new empty file and upload it similarly as you do for the given file.

file1 = open('List.txt', 'r')
file2 = open('List2.txt', 'w')
content = file1.readlines()
for i in range(1, len(content) + 1):
    if (i % 2 != 0):
        file2.write(content[i - 1])
    else:
        pass
file1.close()
file2.close()