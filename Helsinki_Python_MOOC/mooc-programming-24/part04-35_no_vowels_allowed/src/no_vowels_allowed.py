# Write your solution here
def no_vowels(string):
    vowels = 'aeiou'
    for char in vowels:
        string = string.replace(char, '')
    return string