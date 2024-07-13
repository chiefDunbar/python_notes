# write your solution here
def matrix_sum():
    sum_ = 0
    for row in generate_matrix('matrix.txt'):
        sum_ += sum(row)
    return sum_

def matrix_max():
    max_ = 0
    start = True
    for row in generate_matrix('matrix.txt'):
        if start or max(row) > max_:
            max_ = max(row)
            start = False
    return max_

def row_sums():
    row_sums_ = []
    for row in generate_matrix('matrix.txt'):
        row_sums_.append(sum(row))
    return row_sums_

def generate_matrix(name):
    with open(name) as file:
        matrix = []
        for row in file:
            num_row = []
            row = row.replace('\n', '').split(',')
            for col in row:
                num_row.append(int(col))
            matrix.append(num_row)
        return matrix
    
if __name__ == '__max__':
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())
    print(generate_matrix('matrix.txt'))
