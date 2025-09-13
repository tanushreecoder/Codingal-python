#Write a Python program to duplicate from one file and then copy it to another file. For copying it in a new file, create a new empty file and upload it in a similar way as you do for the given file.

#Program to eliminate repeated lines

outputfile = open('Updated file.txt', 'w')
inputfile = open('Repeated.txt', 'r')
linesSeenSoFar = set()        #Set ignores the duplicates and uses it to add new lines
for i in inputfile:
    if i not in linesSeenSoFar:
        outputfile.write(i)
        linesSeenSoFar.add(i)
inputfile.close()
outputfile.close()