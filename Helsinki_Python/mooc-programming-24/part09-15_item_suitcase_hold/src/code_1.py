# Write your solution here:
class Item:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight
    
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
    def __init__(self, maximum_weight):
        self.__maximum_weight = maximum_weight
        self.__items = []

    def add_item(self, item: Item):
        if self.__maximum_weight - self.weight() < item.weight():
            return
        self.__items.append(item)

    def print_items(self):
        for item in self.__items:
            print(item)

    def weight(self):
        return sum(item.weight() for item in self.__items)

    def heaviest_item(self):
        if not self.__items:
            return None
        heaviest = self.__items[0]
        for item in self.__items:
            if item.weight() > heaviest.weight():
                heaviest = item
        return heaviest


    def __str__(self):
        length = len(self.__items)
        if length == 1:
            return f"{length} item ({self.weight()} kg)" 
        return f"{length} items ({self.weight()} kg)"

class CargoHold:
    def __init__(self, maximum_weight):
        self.__maximum_weight = maximum_weight
        self.__suitcases = []
    
    def add_suitcase(self, suitcase: Suitcase):
        if self.__maximum_weight - self.__weight() < suitcase.weight():
            return
        self.__suitcases.append(suitcase)
    
    def __weight(self):
        return sum(suitcase.weight() for suitcase in self.__suitcases)

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def __str__(self):
        if len(self.__suitcases) == 1:
             return f"{len(self.__suitcases)} suitcase, space for {self.__maximum_weight - self.__weight()} kg"
        return f"{len(self.__suitcases)} suitcases, space for {self.__maximum_weight - self.__weight()} kg"
