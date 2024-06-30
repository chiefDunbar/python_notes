# Write your solution here
def first_word(string):
    return string[0:string.find(' ')]

def second_word(string):
    start = string.find(' ') + 1
    string = string[start:]
    end = string.find(' ') 
    if end == -1:
        end = len(string)
    return string[0:end]

def last_word(string):
    string = string[::-1]
    return string[0:string.find(' ')][::-1]


# You can test your function by calling it within the following block
if __name__ == "__main__":
    # sentence = "once upon a time there was a programmer"
    sentence = 'first second'
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))