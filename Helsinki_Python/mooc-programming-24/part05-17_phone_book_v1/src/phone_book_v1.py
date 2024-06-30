# Write your solution here
phonebook = {}
while True:
    command = int(input('command (1 search, 2 add, 3 quit): '))
    if command == 1:
        name = input('name: ')
        if name not in phonebook:
            print('no number')
            continue
        print(phonebook[name])
    elif command == 2:
        name = input('name: ')
        phonebook[name] = input('number: ')
        print('ok!')
    elif command == 3:
        print('quitting...')
        break