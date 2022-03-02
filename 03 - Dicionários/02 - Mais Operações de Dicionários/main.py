def __main__():
    phrase = "I love programming and I want learning more and more languages to expand my knowledge"

    words = phrase.split()

    set_phrase = set(words)
    print(set_phrase)

    words = {
        "I": 2,
        "love": 1,
        "want": 1,
        "and": 2
    }
    print(words["I"])
    print(words["love"])

    # The "del" delete the key and value from dictionary if exists
    del words["love"]
    print(words)

    # To verify if an element exists in the dictionary, put the KEY followed by "in" and the dictionary name
    print("I" in words)

    for key in words:
        print(key)

    # To access the keys of the dictionary, just put the ".keys()" function
    for key in words.keys():
        print(key)

    # To access the values of the dictionary, just put the ".values()" function
    for key in words.values():
        print(key)

    # To access the items (key value) of the dictionary, just put the ".items()" function
    for key in words.items():
        print(key)

    # To access the items (key value) of the dictionary, just put the ".items()" function
    for key, value in words.items():
        print(key, ":", value)


if __name__ == "__main__":
    __main__()
