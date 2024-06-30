# write your solution here
dictionary = []
with open('wordlist.txt') as file:
    for word in file:
        word = word.strip()
        dictionary.append(word)

sentence = input('Write text: ')

words = sentence.split(' ')
sentence = ''
for index in range(0, len(words)):
    if words[index].lower() not in dictionary:
        sentence += f' *{words[index]}*'
    else:
        sentence += f' {words[index]}'

print(sentence.strip())



    

