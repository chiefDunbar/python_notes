# Write your solution here
def length_of_longest(strings):
    length = 0
    for string in strings:
        if len(string) > length:
            length = len(string)
    return length