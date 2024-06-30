# Write your solution here
def create_tuple(x: int, y: int, z: int):
    order = [x, y, z]
    return (min(order), max(order), sum(order))