#Write a Python program to merge the contents of two different files into a third file. Create this new third file first and then copy the contents.

with open('Repeated.txt', 'r') as r:
    data1 = r.read()
with open('Updated file.txt', 'r') as u:
    data2 = u.read()
data1 += "\n"
data1 += data2             #This means data1 = data1 + data2
with open('MergedFile.txt', 'w') as file:
    file.write(data1)
    