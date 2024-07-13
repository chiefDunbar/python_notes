# Write your solution here
from difflib import get_close_matches

# write your solution here
reference = []
with open('wordlist.txt') as file:
    for word in file:
        word = word.strip()
        reference.append(word)

sentence = input('write text: ')

words = sentence.split(' ')
sentence = ''
suggestions = {}

for word in words:
    if word.lower() not in reference:
        sentence += f' *{word}*'
        suggestions[word] = get_close_matches(word, reference)
    else:
        sentence += f' {word}'

print(sentence.strip())
print("suggestions:")
for word, suggested_words in suggestions.items():
    suggested_words = ", ".join(suggested_words)
    print(f"{word}: {suggested_words}")




    

