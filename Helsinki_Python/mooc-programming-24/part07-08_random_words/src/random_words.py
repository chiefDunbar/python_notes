# Write your solution here
from random import shuffle
def words(n, beginning):
    
    words = []
    with open('words.txt') as file:
        for row in file:
            row = row.strip()
            if row.startswith(beginning) and row not in words:
                words.append(row)
    
    if len(words) < n:
        raise ValueError
    
    result = []
    counter = 0
    while counter < n and len(words) > 0:
        shuffle(words)
        result.append(words[0])
        words = words[1:]
        counter += 1
    
    if counter < n:
        raise ValueError
    
    return result


if __name__ == '__word__':
    word_list = words(3, "ca")
    for word in word_list:
        print(word)
    