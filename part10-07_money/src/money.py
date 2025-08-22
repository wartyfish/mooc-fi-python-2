class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
        self.__amount = euros*100 + cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, other):
        return (self.__euros == other.__euros and self.__cents == other.__cents)

    def __gt__(self, other):
        return self.__amount > other.__amount

    def __lt__(self, other):
        return self.__amount < other.__amount

    def __ne__(self, other):
        return self.__amount != other.__amount

    def __add__(self, other):
        r_euros, r_cents = divmod((self.__amount + other.__amount), 100)
        result = Money(r_euros, r_cents)     
        return result.__str__()

    def __sub__(self, other):
        if self.__amount > other.__amount:
            r_euros, r_cents = divmod((self.__amount - other.__amount), 100)
            result = Money(r_euros, r_cents)     
            return result.__str__()
        else:
            raise ValueError("a negative result is not allowed")

if __name__ == "__main__":
    e1 = Money(4, 10)
    e2 = Money(2, 5)

    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)
    print(e1 + e2)
    print(e1 - e2)
    print(e2 - e1)