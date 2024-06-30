# Write your solution here
from random import choice
from string import ascii_lowercase, digits
def generate_strong_password(length: int, include_numbers: bool, include_special_characters: bool):
    password = ''
    special_characters= "!?=+-()#"
    counter = 0
    while counter < length:
        password += choice(ascii_lowercase)
        counter += 1
        if include_numbers and counter < length:
            password += choice(digits)
            counter += 1
        if include_special_characters and counter < length:
            password += choice(special_characters)
            counter += 1
    return password

if __name__ == '__main__':
    for i in range(10):
        print(generate_strong_password(8, False, False))