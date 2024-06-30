# Write your solution here
def factorials(n: int):
    dictionary = dict()
    for key in range(1, n + 1):
        value = 1
        for index in range(key, 1, -1):
            value *= index
        dictionary[key] = value
    return dictionary

# next solution is dependent of previous solutions: dynamic programming?
# def factorials(n: int):
#     result = {}
#     result[1] = 1
#     for i in range(2, n + 1):
#         result[i] = result[i - 1] * i
#     return result