# Write your solution here
def row_correct(sudoku: list, row_no: int):
    unique = []
    row = sudoku[row_no]
    for element in row:
        if element != 0:
            if element not in unique:
                unique.append(element)
            else:
                return False
    return True


def column_correct(sudoku: list, column_no: int):
    unique = []
    for row in sudoku:
        if row[column_no] != 0:
            if row[column_no] not in unique:
                unique.append(row[column_no])
            else:
                return False
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    unique = []
    for row in range(row_no, row_no + 3):
        for col in range(column_no, column_no + 3):
            if sudoku[row][col] != 0:
                if sudoku[row][col] not in unique:
                    unique.append(sudoku[row][col])
                else:
                    return False
    return True

def sudoku_grid_correct(sudoku: list):
    for index in range(0, 9):
        if not row_correct(sudoku, index) or not column_correct(sudoku, index):
            return False
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if not block_correct(sudoku, row, col):
                return False
    return True
