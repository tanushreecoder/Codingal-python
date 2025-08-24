class Employee:   #Creating class employee
    def __init__(self):   #Initializing (Constructor)
        print("Employee created")
    def __del__(self):   #Deleting (Destructor)
        print("Deconstructer is called, employee is deleted")
obj = Employee()
del obj