from collections import Counter


def __main__():
    text = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque optio nobis hic accusamus quia, ducimus eius odio consectetur magni dolor saepe deserunt libero nam eaque laborum non assumenda aliquam. Iusto."
    print(text.split())

    print(Counter(text.lower()))
    print(sum(Counter(text).values()))


if __name__ == "__main__":
    __main__()
