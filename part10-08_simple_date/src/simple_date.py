class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year
        self.__days = day + month*30 + year*360
        
    def dateify(self, days: int):
        y, md = divmod(days, 360)
        m, d = divmod(md, 30)

        return SimpleDate(d, m, y)
    
    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

    def __eq__(self, other: "SimpleDate"):
        return self.__days == other.__days

    def __ne__(self, other: "SimpleDate"):
        return self.__days != other.__days
    
    def __gt__(self, other: "SimpleDate"):
        return self.__days > other.__days
    
    def __lt__(self, other: "SimpleDate"):
        return self.__days < other.__days

    def __add__(self, incriment: int):
        d = self.__days + incriment 
        
        return self.dateify(d)

    def __sub__(self, other: int):
        diff = abs(self.__days - other.__days)
        return diff

if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d1 + 1)