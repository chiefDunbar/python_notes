# Write your solution here
words = list()
while True:
    word = input('Word: ')
    if word not in words:
        words.append(word)
    else:
        print(f'You typed in {len(words)} different words')
        break