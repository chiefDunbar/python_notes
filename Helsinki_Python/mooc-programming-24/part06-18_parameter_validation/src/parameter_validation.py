# Write your solution here
def new_person(name: str, age: int):
    name_length = len(name)
    if name_length == 0 or name_length > 40  or len(name.split()) < 2 or age < 0 or age > 150:
        raise ValueError()
    return(name, age)