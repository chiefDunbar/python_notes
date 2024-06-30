# Write your solution here
# You can test your function by calling it within the following block
def greatest_number(one, two, three):
    if one >= two and one >= three:
        return one
    elif two >= one and two >= three:
        return two
    else:
        return three
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)