# Write your solution here
def distinct_numbers(_list: list):
    new_list = list()
    for item in _list:
        if item not in new_list:
            new_list.append(item)
    return sorted(new_list)