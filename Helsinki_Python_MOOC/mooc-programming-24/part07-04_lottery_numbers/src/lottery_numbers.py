# Write your solution here
import random
def lottery_numbers(amount: int, lower: int, upper: int):
    numbers = []
    counter = 0
    while counter < amount:
        number = random.randint(lower, upper)
        if number not in numbers:
            numbers.append(number)
            counter += 1
    return sorted(numbers)

# for number in lottery_numbers(7, 1, 40):
#     print(number)