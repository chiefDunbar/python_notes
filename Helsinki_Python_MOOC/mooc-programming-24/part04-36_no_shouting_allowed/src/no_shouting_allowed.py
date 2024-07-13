# Write your solution here
def no_shouting(strings):
    small_case = []
    for string in strings:
        if not string.isupper():
            small_case.append(string)
    return small_case