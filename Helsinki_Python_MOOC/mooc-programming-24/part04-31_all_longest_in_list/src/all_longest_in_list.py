# # Write your solution here
# def all_the_longest(strings):
#     longest = 0
#     longest_list = list()
#     for string in strings:
#         if len(string) > longest:
#             longest = len(string)
#     for string in strings:
#         if len(string) == longest:
#             longest_list.append(string)
#     return longest_list

def all_the_longest(strings):
    result = list()

    for string in strings:
        if result == [] or len(string) > len(result[0])
            result = [string]
        elif len(string) == len(result[0]):
            result.append(string)
    return result