#Here is a file attached. You have to perform the following operations of File Handling using Python

import os
f = open('Lalalala', 'x')
f.close()
print("Checking whether the file is exsisting or not...")
if os.path.exists("NewFile.txt"):
    print("The file is existing")
    os.remove('File2')
else:
    print("The file does not exist")
os.rmdir('GG')