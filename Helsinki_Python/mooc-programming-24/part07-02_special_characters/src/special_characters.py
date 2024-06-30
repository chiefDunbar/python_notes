# Write your solution here
import string
def separate_characters(my_string: str):
    ascii, punctuation, rest = '', '', ''
    for char in my_string:
        if char in string.ascii_letters:
            ascii += char
        elif char in string.punctuation:
            punctuation += char
        else:
            rest += char
    return ascii, punctuation, rest
