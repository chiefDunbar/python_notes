# Write your solution here

def load_file(filename: str):
    recipes = []
    with open(filename) as file:
        recipe = []
        for row in file:
            if row.strip() == '':
                recipes.append(recipe)
                recipe = []
                continue
            recipe.append(row.strip())
        recipes.append(recipe)
    return recipes

def search_by_name(filename: str, word: str):
    recipes = load_file(filename)
    result = []
    for recipe in recipes:
        if recipe[0].lower().find(word.lower()) != -1:
            result.append(recipe[0])
    return result

def search_by_time(filename: str, prep_time: int):
    recipes = load_file(filename)
    result = []
    for recipe in recipes:
        if int(recipe[1]) <= prep_time:
            result.append(f'{recipe[0]}, preparation time {recipe[1]} min')
    return result

def search_by_ingredient(filename: str, ingredient: str):
    recipes = load_file(filename)
    result = []
    for recipe in recipes:
        for items in recipe[2:]:
            if items.lower().find(ingredient.lower()) != -1:
                result.append(f'{recipe[0]}, preparation time {recipe[1]} min')
    return result

