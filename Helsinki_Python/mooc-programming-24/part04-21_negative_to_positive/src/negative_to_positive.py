# Write your solution here
limit = int(input('Please type in a positive integer: '))
for num in range(-limit, limit + 1):
    if num == 0:
        continue
    print(num)