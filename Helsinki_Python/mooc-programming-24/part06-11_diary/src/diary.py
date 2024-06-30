# Write your solution here

while True:
    print('1 - add an entry, 2 - read entries, 0 - quit')
    choice = input('Fuction: ')
    if choice == '1':
        with open('diary.txt', 'a') as diary:
            entry = input('Diary entry: ')
            diary.write(f'{entry}\n')
        print('Diary Saved\n')
    if choice == '2':
        print('Entries:')
        with open('diary.txt') as diary:
            for line in diary:
                print(line.strip())
    if choice == '0':
        print('Bye now!')
        break

