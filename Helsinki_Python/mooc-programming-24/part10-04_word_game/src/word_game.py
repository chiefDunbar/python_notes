# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else:
            return None

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def __count_vowels(self, word):
        vowels = "aeiou"
        word = word.lower()
        count = 0
        for vowel in vowels:
            count += word.count(vowel)
        return count

    def round_winner(self, player1_word: str, player2_word: str):
        player1_count = self.__count_vowels(player1_word)
        player2_count = self.__count_vowels(player2_word)
        if player1_count > player2_count:
            return 1
        elif player2_count > player1_count:
            return 2
        else:
            return None

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        
        check = self.__check_validity(player1_word, player2_word)
        if check != 0:
            return check
        
        win = {"rock": "scissors", "paper":"rock", "scissors": "paper"}

        if win[player1_word] == player2_word:
            return 1
        elif win[player2_word] == player1_word:
            return 2 
        else:
            return None

    def __check_validity(self, response_one, response_two):
        valid_responses = ['rock', 'paper', 'scissors']
        if response_one not in valid_responses and response_two not in valid_responses:
            return None
        elif response_one not in valid_responses:
            return 2
        elif response_two not in valid_responses:
            return 1
        return 0    

if __name__ == "__main__":
    game = RockPaperScissors(4)
    game.play()
