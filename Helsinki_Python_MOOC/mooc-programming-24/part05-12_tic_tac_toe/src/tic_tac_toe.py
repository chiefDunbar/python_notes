# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if 0 <= y <= 2 and 0 <= x <= 2:
        if game_board[y][x] == '':
            game_board[y][x] = piece
            return True
    return False