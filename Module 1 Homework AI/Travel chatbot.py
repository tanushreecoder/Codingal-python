import re, random

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
    print("Travel bot: Where to?")
    location = normalize_input(input("You: "))
    print("Travelbot: For how many days?")
    days = input("You: ")
    print(f"Travelbot: Packing tips for {days} for {location}: ")
    print("1. Pack versatile clothes")
    print("2. Bring chargers/adapters")
    print("3. Check the weather forecast")
def joke():
    print(random.choice(jokes))
def show_help():
    print("\n I can:")
    print("Suggest travel spots(say 'Recomendation')")
    print("Offer tips for packing (say 'Packing')")
    print("Tell you a joke (say 'joke')")
    print("Or you can end the chat by typing 'exit' or 'bye'\n")
def chat():
    print("Hello, I'm Travelbot")
    name = input("Your name? ")
    print(f"Nice to meet you {name}!")
    show_help()
while True:
    user_input = input(f"{__name__}: ")
    user_input = normalize_input(user_input)
    if "Recomendation" in user_input or "Suggest" in user_input:
        recommend()
    elif "Packing" in user_input or "Pack" in user_input:
        packing_tips()
    elif "joke" in user_input:
        jokes()
    elif "Help" in user_input:
        show_help()
    elif "Exit" in user_input:
        print("Travel safe!")
    else:
        print("I couldn't understand, could you reprase?")


    if __name__ == "__main__":
        chat()