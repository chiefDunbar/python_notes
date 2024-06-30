# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week: int, correct: list):
        self.week = week
        self.correct = correct

    def number_of_hits(self, numbers: list):
        return len([number for number in numbers if number in self.correct])
    
    def hits_in_place(self, numbers: list):
        return [number if number in self.correct else -1 for number in numbers]