# Write your solution here
def list_sum(one: list, two: list):
    three = []
    for index in range(len(one)):
        three.append(one[index] + two[index])
    return three

for i, j in zip(one, two):
    three.append(i + j)