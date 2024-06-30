# Write your solution here
from random import choice

def roll(die: str):
    if die == 'A':
        faces = [3, 3, 3, 3, 3, 6]
    if die == 'B':
        faces = [2, 2, 2, 5, 5, 5]
    if die == 'C':
        faces = [1, 4, 4, 4, 4, 4]
    return choice(faces)

def play(die1, die2, times):
    counter_one, counter_two = 0, 0
    for index in range(times):
        r1, r2 = roll(die1), roll(die2)
        if r1 > r2:
            counter_one += 1
        elif r2 > r1:
            counter_two += 1
    return counter_one, counter_two, times - (counter_one + counter_two)
if __name__ == '__main__':
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)