# Write your solution here
def column_correct(sudoku: list, column_no: int):
    unique = []
    for row in sudoku:
        if row[column_no] != 0:
            if row[column_no] not in unique:
                unique.append(row[column_no])
            else:
                return False
    return True