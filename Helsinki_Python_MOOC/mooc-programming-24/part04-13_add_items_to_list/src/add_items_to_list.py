# Write your solution here
count = int(input('How many items: '))
items = []
index = 0
while index < count:
    items.append(int(input(f'Item {index + 1}: ')))
    index += 1
print(items)