def __main__():
    phrase = "I love programming and I want learning more and more languages to expand my knowledge"

    words = phrase.split()

    set_phrase = set(words)
    print(set_phrase)

    # The dictionary is consists of key value sets
    dictionary = {
        "I": 2,
        "love": 1
    }

    # To access the values of the dictionary, just put the key between the "[]"
    print(dictionary["I"])
    print(dictionary["love"])

    # To create a dictionary, just put the "key=" with the key, and the "value=" with the value
    dictionary = dict(key="I", value=2)
    print(dictionary)


if __name__ == "__main__":
    __main__()
