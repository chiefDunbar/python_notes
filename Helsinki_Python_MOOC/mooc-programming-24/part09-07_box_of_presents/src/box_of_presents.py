# WRITE YOUR SOLUTION HERE:
class Present:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight 
    
    def __str__(self):
        return f"{self.name} ({self.weight} kg)"

class Box:

    def __init__(self):
        self.presents = []

    def add_present(self, present: Present):
        self.presents.append(present)
    
    def total_weight(self):
        result = 0
        for present in self.presents:
            result += present.weight
        return result