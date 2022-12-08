import json


def task():
    filename = "input.json"
    with open(filename) as fn:
        dict_ = json.load(fn)
        max_v = max(dict_, key=lambda x: x["score"])

    # TODO считать содержимое JSON файла

    return max_v     # TODO найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
