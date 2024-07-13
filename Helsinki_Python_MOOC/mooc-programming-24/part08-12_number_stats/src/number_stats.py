# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)
    
    def get_sum(self):
        if self.count_numbers() == 0:
            return 0
        return sum(self.numbers)

    def average(self):
        if self.count_numbers() == 0:
            return 0
        return self.get_sum() / self.count_numbers()

all = NumberStats()
even = NumberStats()
odd = NumberStats()

print('Please type in integer number:')
while True:
    num = int(input())
    if num == -1:
        break
    if num % 2 == 0:
        even.add_number(num)
    else:
        odd.add_number(num)
    all.add_number(num)

print("Sum of numbers:", all.get_sum())
print("Mean of numbers:", all.average())
print("Sum of even numbers:", even.get_sum())
print("Sum of odd numbers:", odd.get_sum())