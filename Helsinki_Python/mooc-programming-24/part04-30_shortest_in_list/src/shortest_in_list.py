# Write your solution here
def shortest(strings):
    length = len(strings[-1])
    shortest = str()
    for index in range(len(strings) - 1):
        if len(strings[index]) < length:
            length = len(strings[index])
            shortest = strings[index]
    return shortest