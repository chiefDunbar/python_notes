# Write your solution here
def even_numbers(_list):
    new_list = list()
    for item in _list:
        if item % 2 == 0:
            new_list.append(item)
    return new_list