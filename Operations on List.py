#List
list = [30, 73, 7, 38]
#Dictionary
dictionary = {"name": "Timmy", "Grade": 2}
#Tuple
tuple = (20, 84, 83)
#Set
set = {32, 32, 8, 8, 3, 92, 83, 83, 84, 62}
print(f"List: {list}, Dictionary: {dictionary}, tuple: {tuple}, set: {set}")
names = ["Nashmia", "Shubrota", "Yearika", "Fayhaa"]
print(names)
names.append("Saba")
print(names)
names.pop(2)
print(names)
names.remove("Nashmia")
print(names)
names.sort()
print(names)
names.reverse()
print(names)
names.clear()
print(names)
player = {"name": "Messi", "Game": "Football", "Age": 39, "WC winner": 1}
print("\nPlayer profile:", player)
print("Age: ", player["Age"])
print("WC winner: ", player.get("WC winner", "Not found"))
player["WC winner"] = 2
player["Nationality"] = "Argentina"
player.pop("Game")
print("Updated player profile: ", player)
age = [1, 7, 8, 6, 20, 3]
names = ["Lily", "Danny", "Kenny", "Figgy", "Jerry", "Tom"]
nd = dict(zip(age, names))
print("\nAges of people", nd)
print("Age of 4th: ", nd[4])