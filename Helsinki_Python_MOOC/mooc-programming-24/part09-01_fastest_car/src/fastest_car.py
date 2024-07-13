# Write your solution after the class Car
# Do not make changes to the class!
class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"

# WRITE YOUR SOLUTION HERE:
def fastest_car(cars: list):
    max = [0, '']
    for car in cars:
        if car.top_speed > max[0]:
            max[0] = car.top_speed
            max[1] = car.make
    return max[1]