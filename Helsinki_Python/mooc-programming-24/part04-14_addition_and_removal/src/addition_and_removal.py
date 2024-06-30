# Write your solution here
numbers = []

while True:
    print('The list is now', numbers)
    choice = input('a(d)d, (r)emove or e(x)it: ')
    if choice == 'd':
        if len(numbers) == 0:
            numbers.append(1)
        else:
            numbers.append(numbers[-1] + 1)
    elif choice == 'r':
        numbers.pop(-1)
    elif choice == 'x':
        break
print('Bye!')
