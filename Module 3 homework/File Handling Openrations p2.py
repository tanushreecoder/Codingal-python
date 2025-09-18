import os
f = open('Happy happy happy', 'x')
f.close()
if os.path.exists("NewFile.txt"):
    print("The file is existing")
    os.remove('File2')
else:
    print("The file does not exist")
os.rmdir('GG')