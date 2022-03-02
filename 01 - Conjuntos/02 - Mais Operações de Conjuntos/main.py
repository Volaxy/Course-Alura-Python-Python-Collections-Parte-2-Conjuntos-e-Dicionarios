def __main__():
    data_science_users = [15, 23, 43, 56]
    machine_learning_users = [13, 23, 35, 21, 43]

    watched = data_science_users.copy()
    watched.extend(machine_learning_users)

    data_science_users = set(data_science_users)
    machine_learning_users = set(machine_learning_users)

    print(set(watched))
    print(data_science_users & machine_learning_users)
    print(data_science_users - machine_learning_users)


if __name__ == "__main__":
    __main__()
