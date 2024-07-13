# # Write your solution here
# def most_common_character(string):
#     string = string[::-1]
#     max_frequency = 0
#     max_frequency_char = ''
#     for char in string:
#         if string.count(char) > max_frequency:
#             max_frequency_char = char
#             max_frequency  = string.count(char)
#     return max_frequency_char

#print(most_common_character('abcdbde'))

# Write your solution here
def most_common_character(string):
    #string = string[::-1]
    unique = []
    max_frequency = 0
    max_frequency_char = ''
    for char in string:
        if char not in unique and string.count(char) > max_frequency:
            unique = [char]
            max_frequency_char = char
            max_frequency  = string.count(char)
    return max_frequency_char

