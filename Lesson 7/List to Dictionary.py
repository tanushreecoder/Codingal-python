def conversion(list): #Conversion function definition
    result = {} #Initialized the dictionary as empty
    for item in list:
        result[item[0]] = item[1:] 
    return result
students = [[1, 'Tanushree', 'Saha'], [2, 'Yearika', 'Fahmin'], [3, 'Wania', 'Chowdhury']]
print("Original list of list is", students)
print("The converted list to a dictionary is", conversion(students)) #Function called as wel a paremeter is passed