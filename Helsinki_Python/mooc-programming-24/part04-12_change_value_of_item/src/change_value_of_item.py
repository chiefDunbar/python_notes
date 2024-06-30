# Write your solution here
numbers = [1, 2, 3, 4, 5]
while True:
    index = int(input('Index: '))
    if index == -1:
        break
    if index >= 5:
        continue
    new_value = int(input('New values: '))
    numbers[index] = new_value
    print(numbers)