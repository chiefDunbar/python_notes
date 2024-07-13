# Write your solution here
def same_chars(string, one, two):
    if one < 0 or one >= len(string) or two < 0 or two >= len(string) or string[one] != string[two]:
        return False
    else:
        return True
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))