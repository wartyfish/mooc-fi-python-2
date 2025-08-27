def lengths(strings: list):
    return {string: len(string) for string in strings}

if __name__ == "__main__":
    strings = ["hello", "world", "this", "is", "a", "list"]
    print(lengths(strings))