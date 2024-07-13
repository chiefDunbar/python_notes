# Write your solution here
def double_items(numbers: list):
    copy = numbers[:]
    for index in range(0, len(copy)):
        copy[index] *= 2
    return copy
