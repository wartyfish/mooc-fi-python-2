class Recording:
    def __init__(self, length: int):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("Value Error, length cannot be negative")
    
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, length: int):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("Value Error, length cannot be negative")
if __name__ == "__main__":
    cd = Recording(69)
    print(cd.length)
    cd.length = -1    
    print(cd.length)