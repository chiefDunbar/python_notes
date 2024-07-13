# Write your solution here
def sum_of_positives(my_list):
    my_list.sort()
    sum = 0
    for num in my_list:
        if num > 0:
            sum += num 
    return sum
if __name__ == '__main__':
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print('The result is', result)
