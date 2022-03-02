from collections import defaultdict, Counter


def __main__():
    phrase = "I love programming and I want learning more and more languages to expand my knowledge"

    words = phrase.split()
    print(words)

    apparitions = defaultdict(int)

    for word in words:
        apparitions[word] += 1
    print(apparitions)

    new_items = defaultdict(int)

    # It's possible access the index without have any object inside the dictionary, in the "defaultdict"
    print(new_items[15])
    print(new_items[5])
    print(new_items[20])

    # The "Counter()" counts the appearance of each element
    print(Counter(words))


if __name__ == "__main__":
    __main__()
