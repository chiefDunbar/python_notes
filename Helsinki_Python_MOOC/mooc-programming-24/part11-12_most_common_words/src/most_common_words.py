# WRITE YOUR SOLUTION HERE:
import string
def most_common_words(filename: str, lower_limit: int):
    with open(filename) as file:
        contents = "".join([character for character in file.read().replace("\n", " ") if character not in string.punctuation]).split(" ")
        return {word: contents.count(word) for word in contents if contents.count(word) >= lower_limit}
