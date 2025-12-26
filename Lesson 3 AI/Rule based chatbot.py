import re, random
import Fore, init
init(autoreset=True)
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss apls", "Rocky mountains", "Himalayas"],
    "cities" : ["Tokyo", "Paris", "New York"]
}
jokes = [
    "Why don't programmers like nature? Because there's too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do traverlers always feel warm? Because of their hot spots!"
]
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())
def recommend():
    print("Travelbot: Beaches, mountains or cities")
    preference = input("You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(f"Travelbot: How about {suggestion}")
        print(f"Do you like it? (yes/no)")
        answer = input("You: ")

        if answer == "yes":
            print(f"Travelbot: Awesome! Enjoy {suggestion}")
        elif answer == "no":
            print("Travelbot: Okay, Let's try another")
            recommend()
        else:
            print("Travelbot: I'll suggest again")
            recommend()
    else:
        print("Sorry, I don't have that type of destination")
        show_help()
def packing_tips():
    