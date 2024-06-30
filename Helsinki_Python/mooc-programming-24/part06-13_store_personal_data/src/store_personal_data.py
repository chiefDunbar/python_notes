# Write your solution here

def store_personal_data(person: tuple):
    with open('people.csv', 'a') as file:
        string = ''
        for detail in person:
            string += (f'{detail};')
        file.write(f'\n{string[:-1]}')
