# Write your solution here:
from random import choice
def word_generator(characters: str, length: int, amount: int):
    #return (''.join([characters[random.randint(0, len(characters) - 1)] for pos in range(length)]) for times in range(amount))
    return (''.join([choice(characters) for _ in range(length)]) for __ in range(amount))