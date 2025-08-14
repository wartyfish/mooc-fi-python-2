class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0

    def add_number(self, number:int):
        self.numbers += number
        self.count += 1

    def count_numbers(self):
        return self.count
    
    def get_sum(self):
        return self.numbers
    
    def average(self):
        avg = (self.numbers / self.count) if self.count != 0 else 0
        return avg

if False:
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())
else:
    nums = NumberStats()
    evens = NumberStats()
    odds = NumberStats()

    print("Please type in integer numbers:")
    while True:
        inpt = int(input())
        if inpt == -1:
            break
        nums.add_number(inpt)
        evens.add_number(inpt) if inpt % 2 == 0 else odds.add_number(inpt)
    
    print("Sum of numbers:", nums.get_sum())
    print("Mean of numbers:", nums.average())
    print("Sum of even numbers:", evens.get_sum())
    print("Sum of odd numbers:", odds.get_sum())

