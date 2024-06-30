# # Write your solution here
# # ascii A = 65, Z = 90
# # chr(value)
# n = int(input("Layers: "))

# for row in range (1, (2 * n)):
#     row_diff = abs(row - n)
#     for col in range(1, (2 * n)):
#         col_diff = abs(col - n)
#         if row_diff < col_diff:
#             print(chr(65 + col_diff), sep = '', end = '')
#         else:
#             print(chr(65 + row_diff), sep = '', end = '')
#     print()

n = int(input("Layers: "))
 
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
left = ""    # section, that goes downwards
right = ""    # section, that goes upwards
k = n-1       # the location of next character in alphabets
m = 2*n-1     # the number of characters in between
while k >= 1:
    left = left+alphabets[k]
    right = alphabets[k]+right
    m -= 2
    print(left+alphabets[k]*m+right)
    k -= 1
while k <= n-1:
    print(left+alphabets[k]*m+right)
    left = left[:-1]
    right = right[1:]
    m += 2
    k += 1