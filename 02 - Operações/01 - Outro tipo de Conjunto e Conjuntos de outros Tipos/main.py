def __main__():
    users = {4, 8, 3, 6, 8, 9, 1, 5}
    print(users)

    users.add(7)
    # A set does not add repeated elements
    users.add(4)
    print(users)

    users = frozenset(users)
    # The "frozenset" does not alter the set
    # users.add(5)

    print(users)


if __name__ == "__main__":
    __main__()
