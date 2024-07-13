# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name):
        self.__name = name
        self.__observations = []
        self.__counter = 0

    def add_observation(self, observation: str):
        self.__observations.append(observation)
        self.__counter += 1
    
    def latest_observation(self):
        return self.__observations[-1] if self.__observations else ""
    
    def number_of_observations(self):
        return self.__counter
    
    def __str__(self):
        return f"{self.__name}, {self.number_of_observations()} observations"

