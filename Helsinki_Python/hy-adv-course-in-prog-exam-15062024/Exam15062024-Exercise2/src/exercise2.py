# Write your solution to exercise 2 here
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
    

class RecipeBook:

    def __init__(self):
        self.__recipe_book = []

    def __str__(self):
        string = "RecipeBook:"
        for recipe in self.__recipe_book:
            string += f"\n{recipe}" 
        return string

    def add_recipe(self, recipe: Recipe):
        self.__recipe_book.append(recipe)
    
    def remove_recipe(self, recipe: Recipe):
        if recipe in self.__recipe_book:
            self.__recipe_book.remove(recipe)
    
    def recipe_by_name(self, name: str) -> Recipe:
        for recipe in self.__recipe_book: 
            if recipe.name == name:
                return recipe
        return None

    def recipes_containing_ingredients(self, specified_ingredients: list) -> list:
        return [recipe for recipe in self.__recipe_book if all(ingredient in recipe.ingredients for ingredient in specified_ingredients)]
    
    def recipes_within_time(self, limit: int) -> list:
        return [recipe for recipe in self.__recipe_book if recipe.time <= limit]

    def recipes_with_all_ingredients(self, specified_ingredients: list) -> list:
        return [recipe for recipe in self.__recipe_book if all(ingredient in specified_ingredients for ingredient in recipe.ingredients)]

    def all_recipes(self) -> list:
        return self.__recipe_book[:]
