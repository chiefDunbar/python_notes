# WRITE YOUR SOLUTION HERE:
class Recording:
    def __init__(self, length):
        if length < 0:
            raise ValueError("The length should be greater than zero!")
        self.__length = length
    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self, length):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("The length should be greater than zero!")