# Write your solution here
def palindromes(string):
    if string == string[::-1]:
        return True
    else:
        return False

while True:
    string = input('Please type in a palindrome: ')
    if palindromes(string):
        print(f'{string} is a palindrome!')
        break
    else:
        print("that wasn't a palindrome")
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
