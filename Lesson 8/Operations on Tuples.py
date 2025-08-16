tuple1 = () #Empty tuple
tuple2 = (1, 2, 3, 4, 4, 4) #Tuple with intergers
tuple3 = (1, 2, 3, "Hello", "How are you", 67.84)
mytuple = ("Hello", ('tuple2', 2, 3)) #Example of a nested tuple
print(mytuple[0])
print(mytuple[1][1]) #Nested index
x = tuple3[1:5]
print(x)
mytuple = ("Tanushree", "Yearika", "Wanya") #Iteration through tuple datastructure in python
for i in (mytuple):
    print("Hello", i)