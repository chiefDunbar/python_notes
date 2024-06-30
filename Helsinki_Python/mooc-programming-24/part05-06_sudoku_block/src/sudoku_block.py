# Write your solution here
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