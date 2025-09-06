#Write a Python program that can append the content of one file to another file.

file1 = input("Enter the file1 name: ")                     #Entering the filename
file2 = input("Enter the second file name: ")
f1 = open(file1, 'r')           #Opening them
f2 = open(file2, 'r')
print("File 1 Before appending ", f1.read())        #Showing the file before
print("File 2 before appending ", f2.read())
f1.close()
f2.close()
f1 = open(file1, 'a+')
f2 = open(file2, 'r')
f1.write(f2.read())          #Appending the contents of the 1st file to 2nd file
f1.seek(0)
f2.seek(0)
print("File 1 after appending", f1.read())
print("File 2 after appending", f2.read())
f1.close()
f2.close()
