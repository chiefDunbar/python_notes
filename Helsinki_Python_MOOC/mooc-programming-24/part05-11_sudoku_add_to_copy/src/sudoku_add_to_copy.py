# Write your solution here
def print_sudoku(sudoku: list):
    for row in range(0, 9):
        for col in range(0, 9):
            element = sudoku[row][col]
            if element == 0:
                print('_', end='')
            elif 0 <= element <= 9:
                print(f'{element}', end='')
            if col + 1 != 9:
                print(' ', end='')
                if (col + 1) % 3 == 0:
                    print(' ', end='')
        print()
        if (row + 1) % 3 == 0 and row + 1 != 9:
            print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    copied_sudoku = list()
    for row in sudoku:
        copied_row = row[:]
        copied_sudoku.append(copied_row)
    copied_sudoku[row_no][column_no] = number
    return copied_sudoku


if __name__ == '__main__':
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)