def recursive_sum(number: int):
    if number <= 1:
        return number
    return number + recursive_sum(number-1)

if __name__ == "__main__":
    print(recursive_sum(5))