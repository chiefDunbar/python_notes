# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, date: int, month: int, year: int):
        self.__date = date
        self.__month = month
        self.__year = year

    @property
    def date(self):
        return self.__date

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    def __str__(self):
        return f"{self.date}.{self.month}.{self.year}"
    
    def __eq__(self, another):
        return self.date == another.date and self.month == another.month and self.year == another.year
    
    def __nq__(self, another):
        return not self.__eq__(another)
    
    def __lt__(self, another):
        if self.year != another.year:
            return self.year < another.year
        if self.month != another.month:
            return self.month < another.month
        return self.date < another.date
    
    def __gt__(self, another):
        return not self.__eq__(another) and not self.__lt__(another)

    def __add__(self, add_days: int):
        date = self.date + add_days
        month = self.month + (date //30)
        year = self.year + (month // 12)

        date = (date % 30) 
        month = (month % 12)

        return SimpleDate(date, month, year) 
    
    def __sub__(self, another: "SimpleDate"):
        days = self.date - another.date
        months = self.month - another.month
        years = self.year - another.year

        return abs(days + (months * 30) + (years * 360))