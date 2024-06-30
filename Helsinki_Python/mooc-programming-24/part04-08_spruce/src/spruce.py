# Write your solution here
def spruce(height):
    print('a spruce!')
    index = 0
    while index < height:
        print(' ' * (height - index  - 1) + '*' * (index * 2 + 1))
        index += 1
    print(' ' * (height - 1) + '*')
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)