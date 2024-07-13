# Write your solution here
import string
def change_case(orig_string: str) -> str:
    new_string = ''
    for char in orig_string:
        if char.islower():
            new_string += char.upper()
            continue
        new_string += char.lower()
    return new_string

def split_in_half(orig_string: str) -> tuple:
    split = len(orig_string) // 2
    return (orig_string[:split], orig_string[split:])

def remove_special_characters(orig_string: str) -> str:
    new_string = ''
    valid_chars = string.ascii_letters + string.digits + ' '
    for char in orig_string:
        if char not in valid_chars:
            continue
        new_string += char
    return new_string.strip()

if __name__ == '__main__':
    print(change_case('aaa'))