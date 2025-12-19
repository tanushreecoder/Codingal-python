name = input("What's your name?: ")
mood = input(f"Hello {name}, how are you? (Good/Bad): ")
if mood == 'Good':
    print("I'm glad to hear that!")
elif mood == 'Bad':
    print("I'm sorry to hear that, hope things get better.")
else:
    print("It's okay, sometimes it's hard to put feelings into words.")
grade = input(f"Which grade do you read in {name}?: ")
print(f"So you are a {grade}th grader?")
age = input("How old are you?: ")
print("Alright.")
job = input("What do you want to be when you grow up? ")
print(f"You want to be a {job}? Interesting choice")
country = input("What's your dream country? ")
print("Nice choice.")
print(f"So your summary is your name is {name}, your {age} years old, who reads in the {grade}th grade and your mood is {mood}. You want to be a {job} and your dream country is {country}")
print(f"It was nice meeting you {name}. Goodbye!")