class Recipe:
    def __init__(self, name: str, ingredients: list, time: int, instructions: str):
        self.__name = name
        self.__ingredients = ingredients
        self.__time = time
        self.__instructions = instructions

    def __repr__(self):
        return f"Recipe(name='{self.name}', ingredients={self.ingredients}, time={self.time}, instructions='{self.instructions}')"
    
    @property
    def name(self):
        return self.__name
    
    @property
    def ingredients(self):
        return self.__ingredients

    @property
    def time(self):
        return self.__time

    @property
    def instructions(self):
        return self.__instructions

    @name.setter
    def name(self, name: str):
        if type(name) == str and len(name) >= 3:
            self.__name = name

    def __gt__(self, other: "Recipe"):
        return self.time > other.time
    
    def __lt__(self, other: "Recipe"):
        return self.time < other.time
    
    def __eq__(self, other: "Recipe"):
        return self.time == other.time
        
    def __le__(self, other: "Recipe"):
        return self.time <= other.time
    
    def __ge__(self, other: "Recipe"):
        return self.time >= other.time
    