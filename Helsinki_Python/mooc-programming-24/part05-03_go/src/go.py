# Write your solution here
def who_won(game_board: list):
    player_one_count = 0
    player_two_count = 0
    for row in game_board:
        for element in row:
            if element == 1:
                player_one_count += 1
            elif element == 2:
                player_two_count += 1
    
    if player_one_count > player_two_count:
        return 1
    elif player_two_count > player_one_count:
        return 2
    return 0