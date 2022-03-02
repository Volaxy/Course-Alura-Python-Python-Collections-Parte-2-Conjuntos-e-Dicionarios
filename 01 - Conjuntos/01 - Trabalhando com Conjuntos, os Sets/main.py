def __main__():
    data_science_users = [15, 23, 43, 56]
    machine_learning_users = [13, 23, 35, 21]

    # The ".copy()" create a copy of the list
    watched = data_science_users.copy()
    watched.extend(machine_learning_users)

    print(watched)
    print(set(watched))
    # A set is represented by "{x, y, ...}, and not contains indexing"
    print(type({1, 2, 3}))
    # The "|" represents the union of 2 sets
    print(set(data_science_users) | set(machine_learning_users))


if __name__ == "__main__":
    __main__()
