from collections import defaultdict


def __main__():
    phrase = "I love programming and I want learning more and more languages to expand my knowledge"

    words = phrase.split()
    print(words)

    apparitions = {}

    for word in words:
        times = apparitions.get(word, 0)
        apparitions[word] = times + 1
    print(apparitions)

    # To create a dictionary with default values, just use the "defaultdict()", when we want to access a value which not
    # exist
    apparitions = defaultdict(int)

    for word in words:
        times = apparitions[word]
        apparitions[word] = times + 1
    print(apparitions)


if __name__ == "__main__":
    __main__()
