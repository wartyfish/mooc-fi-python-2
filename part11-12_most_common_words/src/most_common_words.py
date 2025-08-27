from string import punctuation

def most_common_words(filename: str, lower_limit: int):
    with open(filename) as f:
        words = []
        for line in f:
            line = line.strip()
            line = "".join(c for c in line if c not in punctuation)
            words += line.split(" ")
        return {w: words.count(w) for w in words if words.count(w) >= lower_limit}


if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))
    