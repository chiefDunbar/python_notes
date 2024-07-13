# Write your solution here
def read_input(string, min_, max_):
    while True:
        try:
            number = int(input(string))
            if min_ <= number <= max_:
                return number
        except ValueError:
            pass
        print(f'You must type in an integer between {min_} and {max_}')
    
if __name__ == '__main__':
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)