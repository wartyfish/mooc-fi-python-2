from collections import Counter

class ListHelper:
    def __init__(self):
        pass

    @classmethod
    def greatest_frequency(cls, my_list: list):
        data = Counter(my_list)
        num, freq = data.most_common(1)[0]
        return num
    
    @classmethod
    def doubles(cls, my_list: list):
        data = Counter(my_list)
        doubles = 0
        for datum in data:
            if data[datum] > 1:
                doubles += 1
        return doubles

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))  