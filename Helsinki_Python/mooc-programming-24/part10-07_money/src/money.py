# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    @property
    def euros(self):
        return self.__euros
    
    @property
    def cents(self):
        return self.__cents

    def __str__(self):
        return f"{self.euros}.{self.cents:02} eur"

    def __eq__(self, another):
        return self.euros == another.euros and self.cents == another.cents

    def __nq__(self, another):
        return not self.__eq__(another)
    
    def __lt__(self, another):
        return self.euros + (self.cents / 100) < another.euros + (another.cents / 100)

    def __gt__(self, another):
        return self.euros + (self.cents / 100) > another.euros + (another.cents / 100)

    def __add__(self, another):
        cents = self.cents + another.cents
        euros = self.euros + another.euros
        if cents >= 100:
            cents -= 100
            euros += 1
        return Money(euros, cents)

    def __sub__(self, another):
        cents = self.cents - another.cents
        euros = self.euros - another.euros
        if cents < 0:
            cents += 100
            euros -= 1
        if euros < 0:
            raise ValueError()
        return Money(euros, cents)
