# Write your solution here
def longest_series_of_neighbours(_list:list):
    longest_series = 0
    sequence = 0
    for index in range(len(_list) - 1):
        if abs(_list[index] - _list[index + 1]) == 1:
            sequence += 1
        else:
            sequence = 0
        if sequence > longest_series:
            longest_series = sequence
    return longest_series + 1

if __name__ == '__main__':
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))