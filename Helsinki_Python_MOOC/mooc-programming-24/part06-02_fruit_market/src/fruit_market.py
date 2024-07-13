# write your solution here
def read_fruits():
    with open('fruits.csv') as fruits:
        prices = {}
        for fruit in fruits:
            fruit = fruit.replace('\n', '').split(';')
            prices[fruit[0]] = float(fruit[1])
        return prices