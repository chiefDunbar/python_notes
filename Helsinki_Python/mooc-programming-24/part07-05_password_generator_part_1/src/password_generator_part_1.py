# Write your solution here
from random import choice
from string import ascii_lowercase
def generate_password(amount: int):
    password = ''
    counter = 0
    while counter < amount:
        password += (choice(ascii_lowercase))
        counter += 1
    return password

