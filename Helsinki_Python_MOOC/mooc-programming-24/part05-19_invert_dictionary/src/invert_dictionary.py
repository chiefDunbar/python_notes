# Write your solution here
def invert(dictionary: dict):
    keys = []
    values = []
    for key, value in dictionary.items():
        keys.append(key)
        values.append(value)
    dictionary.clear()
    for key, value in zip(values, keys):
        dictionary[key] = value

if __name__ == '__main__':
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)