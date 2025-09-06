#Here is a file attached. You have to perform the following operations of File Handling using Python -

file1 = open('Lesson 13/SampleFile.txt', 'r')    #Selecting the file
print(file1.read())       #Python will load the contents of the file as a str or read it
file1.close()     #Closing the file

fileWrite_ = open('Lesson 13/SampleFile.txt', 'w')
fileWrite_.write("What do you want to write?")
fileWrite_.close()

fileAppend = open('Lesson 13/SampleFile.txt', 'a')
fileAppend.write("What do you want to append?")
fileAppend.close() 