# Write your solution here
def histogram(my_str: str):
    distribution = {}
    for character in my_str:
        if character not in distribution:
            distribution[character] = 0
        distribution[character] += 1
    for character, count in distribution.items():
        print(f'{character} ', '*' * count, sep='')

if __name__ == '__main__':
    histogram('statistically')