# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    persons = (person1, person2, person3)
    averages = []
    for person in persons:
        averages.append((person['result1'] + person['result2'] + person['result3']) / 30)
    return persons[averages.index(min(averages))]
      