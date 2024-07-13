# Write your solution here
def longest(strings: list):
    longest_string = ''
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string
if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))