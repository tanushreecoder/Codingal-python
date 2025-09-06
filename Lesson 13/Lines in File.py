#Write a Python program that can calculate and return the total number of lines present inside a file. First, you would be required to read the contents of the file.

file1 = open('Lesson 13/SampleFile.txt')
counter = 0
content = file1.read()
contentList = content.split('\n')
for i in contentList:
    if i :
      counter = counter + 1   #counter+ = 1      #
print(counter)