# Write your solution here
import re

def is_dotw(my_string: str):
    return re.search("^Mon.*|^Tue.*|^Wed.*|^Thu.*|^Fri.*|^Sat.*|^Sun.*", my_string) != None

def all_vowels(my_string: str):
    return re.search("^[aeiou]*$", my_string) != None

def time_of_day(my_string: str):
    return re.search("^([01]\d|2[0-3]):[0-5]\d:[0-5]\d$", my_string) is not None