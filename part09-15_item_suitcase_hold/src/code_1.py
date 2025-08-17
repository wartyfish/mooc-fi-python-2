class Item:
    def __init__(self, name: str, weight: int = 0):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.name()} ({self.weight()} kg)"

class Suitcase:
    def __init__(self, max_weight: int = 0):
        self.max_weight = max_weight
        self.contents = []
        self.__weight = 0
        self.__heaviest_kg = 0
        self.__heaviest_item = None
    
    def add_item(self, item: Item):
        if item.weight() + self.__weight <= self.max_weight:
            self.contents.append(item)
            self.__weight += item.weight()

            if item.weight() > self.__heaviest_kg:
                self.__heaviest_kg = item.weight()
                self.__heaviest_item = item
    
    def __str__(self):
        if len(self.contents) == 1:
            return f"{len(self.contents)} item ({self.__weight} kg)"
        else:
          return f"{len(self.contents)} items ({self.__weight} kg)"
        
    def print_items(self):
        items = []
        for item in self.contents:
            items.append(f"{item.name()} ({item.weight()} kg)")
        
        print("\n".join(items))

    def weight(self):
        return self.__weight

    def heaviest_item(self):
        return self.__heaviest_item
    
class CargoHold:
    def __init__(self, max_weight: int = 0):
        self.max_weight = max_weight
        self.contents = []
        self.__weight = 0
    
    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.weight() + self.__weight <= self.max_weight:
            self.contents.append(suitcase)
            self.__weight += suitcase.weight()

    def __str__(self):
        sgl_plur = "suitcase" if len(self.contents) == 1 else "suitcases"

        return f"{len(self.contents)} {sgl_plur}, space for {self.max_weight - self.__weight} kg"
    
    def print_items(self):
        for suitcase in self.contents:
            suitcase.print_items() 
            

if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()