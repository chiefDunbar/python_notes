# Write your solution here

while True:
    print('1 - Add word, 2 - Search, 3 - Quit')
    function = int(input('Function: '))

    if function == 1:
        with open('dictionary.txt', 'a') as dictionary:
            finnish = input('The word in Finnish: ')
            english = input('The word in English: ')
            dictionary.write(f'{finnish};{english}\n')
            print('Dictionary entry added')
    if function == 2:
        with open('dictionary.txt') as dictionary:
            search_term = input('Search term: ')
            for entry in dictionary:
                if search_term in entry:
                    colon = entry.find(';')
                    print(f'{entry[:colon]} - {entry[colon + 1:].strip()}')
    if function == 3:
        print('Bye!')    
        break
