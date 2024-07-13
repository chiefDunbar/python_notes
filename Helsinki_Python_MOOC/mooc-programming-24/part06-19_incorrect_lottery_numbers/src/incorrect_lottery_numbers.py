def filter_incorrect():
    result = {}
    try:
        with open('lottery_numbers.csv') as file:
            for row in file:
                try:
                    week, numbers = check_validity(row.strip())
                    result[week] = numbers
                except ValueError:
                    pass
    except FileNotFoundError:
        print('File not found!')

    try:
        with open('correct_numbers.csv', 'w') as file:
            for week, numbers in result.items():
                file.write(week)
                number_string = ''
                for number in numbers:
                    number_string += f'{number},'
                file.write(number_string[:-1] + '\n')
    except IOError:
        print("File couldn't be created")

def check_validity(row: str):
    parts = row.split(';')

    week_part, numbers_part = parts
    
    try:
        week = int(week_part[5:])
    except ValueError:
        raise ValueError('Week number is not an integer')
    
    numbers = numbers_part.split(',')
    if len(numbers) != 7:
        raise ValueError('Incorrect number of lottery numbers')
    
    valid_numbers = []
    for number in numbers:
        try:
            num = int(number)
            if num < 1 or num > 39 or num in valid_numbers:
                raise ValueError('Invalid or duplicate number')
            valid_numbers.append(num)
        except ValueError:
            raise ValueError('Non-integer value in numbers')
    
    return (f'week {week};', valid_numbers)
