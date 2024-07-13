# Write your solution here

import json

def print_persons(filename: str):
    persons = []
    with open(filename) as file:
        persons = json.loads(file.read())
    for person in persons:
        hobby_string = f"({', '.join(person['hobbies'])})"
        print(person['name'], f"{person['age']} years", hobby_string, sep = ' ')    