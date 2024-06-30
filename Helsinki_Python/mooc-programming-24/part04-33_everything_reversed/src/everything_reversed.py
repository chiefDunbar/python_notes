# Write your solution here
def everything_reversed(strings:list):
    strings = strings[::-1]
    for (index, string) in enumerate(strings):
        strings[index] = string[::-1]
    return strings