# Write your solution to exercise 3 here
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





class Storage:
    def __init__(self, name: str = "recipes.txt"):
        self.filename = name
        self.recipe_book = RecipeBook()
        self.open_file()
    
    def open_file(self):
        try:
            with open(self.filename, 'r') as file:
                for recipe_text in file:
                    recipe_text = recipe_text.split(';')
                    if len(recipe_text) == 4:
                        name = recipe_text[0]
                        ingredients = recipe_text[1].split(',')
                        time = int(recipe_text[2])
                        instructions = recipe_text[3]
                        self.recipe_book.add_recipe(Recipe(name, ingredients, time, instructions))
        except FileNotFoundError:
            self.reset_memory()
            self.open_file()
            
    def get_recipes(self):
        return self.recipe_book
    
    def write_recipes(self, recipes):
        all_recipes = recipes.all_recipes()
        with open(self.filename, 'w') as file:
            for recipe in all_recipes:
                ingredients = ','.join(recipe.ingredients)
                file.write(f"{recipe.name};{ingredients};{recipe.time};{recipe.instructions}\n")

    def reset_memory(self):
        with open(self.filename, 'w') as file:
            pass








class UserInterface:
    def __init__(self):
        self.storage = Storage("recipes.txt")
        self.recipe_book = self.storage.get_recipes()
        self.run()

    def exit_program(self):
        self.storage.write_recipes(self.recipe_book)
        exit()

    def add_recipe(self):
        name = input("Enter recipe name: ")
        if self.recipe_book.recipe_by_name(name) is None: 
            ingredients = map(lambda x: x.strip(), input("Enter recipe ingredients separated by comma: ").split(','))
            time = int(input("Enter recipe cooktime (min): "))
            instructions = input("Enter recipe instructions: ").strip()
            self.recipe_book.add_recipe(Recipe(name, ingredients, time, instructions))
            print(f"Added recipe {name}")
            return
        print("Recipe already exists")

    def remove_recipe(self):
        name = input("Enter name of recipe to remove: ")
        recipe = self.recipe_book.recipe_by_name(name)
        if recipe is not None:
            self.recipe_book.remove_recipe(recipe)
            print(f"Removed recipe {name}")
            return
        print(f"No recipe found with name {name}")

    def search_recipe_by_name(self):
        name = input("Enter recipe name to search: ")
        recipe = self.recipe_book.recipe_by_name(name)
        if recipe is not None:
            print(f"Found recipe: {recipe}")
            return
        print(f"No recipe found with name {name}")
    
    def search_recipe_by_ingredients(self):
        ingredients = input("Enter the ingredients of the recipe you're looking for, separated by commas: ").split(',')
        recipes = self.recipe_book.recipes_containing_ingredients(ingredients)
        if recipes:
            print(f"Found recipes with ingredients {ingredients}:")
            for recipe in recipes:
                print(recipe)
            return
        print(f"No recipe found with ingredients {ingredients}")
    
    def search_recipe_by_preparation_time(self):
        time = int(input("Enter the preparation time of the recipe you're looking for (min): "))
        recipes = self.recipe_book.recipes_within_time(time)
        if recipes:
            for recipe in recipes:
                print(recipe)
            return
        print(f"No recipe found with preparation time {time} min")

    def search_recipe_by_available_ingredients(self):
        ingredients = input("Enter the ingredients of the recipe you're looking for, separated by commas: ").split(',')
        recipes = self.recipe_book.recipes_with_all_ingredients(ingredients)
        if recipes:
            print(f"Found recipes with ingredients {ingredients}:")
            for recipe in recipes:
                print(recipe)
            return
        print(f"No recipe found with ingredients {ingredients}")

    def return_all_recipes(self):
        recipes = self.recipe_book.all_recipes()
        if recipes:
            print("Found recipes:")
            for recipe in recipes:
                print(recipe)
            return
        print("No recipes found")
    
    def clear_memory(self):
        del self.recipe_book
        self.recipe_book = RecipeBook()
        self.storage.reset_memory()
        print("Memory cleared")

    def print_instructions(self):
        print("Recipe book program")
        print("Commands:")
        commands = ["Exit", 
            "Add recipe", 
            "Remove recipe", 
            "Search recipe by name", 
            "Search recipe by ingredients",
            "Search recipe by preparation time", 
            "Search recipeby available ingredients", 
            "Return all recipes",
            "Clear memory"]
        for num, command in enumerate(commands):
            print(f"{num} - {command}")
    
    def user_input(self):      
        actions = {
            0: self.exit_program,
            1: self.add_recipe,
            2: self.remove_recipe,
            3: self.search_recipe_by_name,
            4: self.search_recipe_by_ingredients,
            5: self.search_recipe_by_preparation_time,
            6: self.search_recipe_by_available_ingredients,
            7: self.return_all_recipes,
            8: self.clear_memory
            }
        try:
            command = int(input("Enter command: "))
            if command not in actions:
                return
            actions[command]()
        except ValueError:
            self.run()
    def run(self):
        self.print_instructions()
        while True:
            self.user_input()

if __name__ == "__main__":
    ui = UserInterface()
    