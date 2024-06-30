# Write your solution here
def older_people(people: list, year: int):
    names = []
    for person in people:
        if person[1] < year:
            names.append(person[0])
    return names