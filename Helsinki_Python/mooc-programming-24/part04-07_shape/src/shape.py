# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def line(length, text):
    if text == '':
        text = '*'
    print( text[0] * length)

def shape(t_height, t_char, r_height, r_char):
    index = 1
    while index <= t_height:
        line(index, t_char)
        index += 1
    index = 1
    while index <= r_height:
        line(t_height, r_char)
        index += 1
if __name__ == "__main__":
    shape(5, "x", 2, "o")