# write your solution here
def largest():
    with open('numbers.txt') as new_file:
        numbers = []
        for number in new_file:
            number = number.replace('\n', '')
            numbers.append(int(number))
        return max(numbers)

def largest():
    with open('numbers.txt') as file:
        start = True
        biggest = 0
        for number in file:
            if start or int(number) > biggest:
                biggest = int(number)
        return biggest
