list = []
x = input("Add things for your checklist. Please add one at a time and when your done, say 'Done'.")
while x != 'Done':
    list.append(x)
    x = input("Add things for your checklist. Please add one at a time and when your done, say 'Done'.")
print("This is your list", list)
print("Now tell me what you have done in those things and we will check it")
y = input("Enter your finished part and when you are done, put 'Finished': ")
while y != 'Finished':
    if y in list:
        list.remove(y)
        print(f"'{y}' has been checked off.")
    else:
        print(f"'{y}' is not in your checklist.")
    y = input("Enter your finished item. When you're done, type 'Finished': ")

if y not in list:
    print("That is not in your list")
else:
    print("Check")

while y != 'Finished':
    list.remove(y)
    y = input("Enter your finished part and when you are done, put 'Finished': ")

if y == "Finished":
    print("Now, this is your list", list)