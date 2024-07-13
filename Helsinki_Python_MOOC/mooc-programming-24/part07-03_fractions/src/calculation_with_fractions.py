# Write your solution here
import fractions

def fractionate(amount: int):
    result = []
    for index in range(amount):
        result.append(fractions.Fraction(1, amount))
    return result
    

def fractionate(amount: int):
    fraction = Fraction(1, amount)
    return [fraction] * amount