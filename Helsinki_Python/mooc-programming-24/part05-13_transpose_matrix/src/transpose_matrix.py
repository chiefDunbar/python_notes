# Write your solution here
def transpose(matrix: list):
    dim = len(matrix)
    for row in range(0, dim):
           for col in range(row, dim):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp

if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]] 
    print(matrix)
    print()
    transpose(matrix)
    print(matrix)