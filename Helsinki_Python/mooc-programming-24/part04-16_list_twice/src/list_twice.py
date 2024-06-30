# Write your solution here
numbers = list()
while True:
    new_item = int(input('New item: '))
    if new_item == 0:
        print('Bye!')
        break
    numbers.append(new_item)
    print(f'The list now: {numbers}')
    print(f'The list in order: {sorted(numbers)}')