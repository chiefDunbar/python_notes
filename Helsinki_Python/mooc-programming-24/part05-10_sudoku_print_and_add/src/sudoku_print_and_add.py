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
            
def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number

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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)    