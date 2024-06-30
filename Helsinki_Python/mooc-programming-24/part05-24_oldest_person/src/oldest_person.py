# Write your solution here
def oldest_person(people: list):
    earliest_year = people[0][1]
    oldest_person = people[0][0]
    for index in range(1, len(people)):
        if people[index][1] < earliest_year:
            earliest_year = people[index][1]
            oldest_person = people[index][0]
    return oldest_person

def oldest_person(people: list):
    oldest = people[0]
    for index in range(1, len(people)):
        if people[index][1] < oldest[1]:
            oldest = people[index]
    return oldest[0]