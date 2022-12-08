import json


def task():
    filename = "input.json"
    with open(filename) as fn:
        words = json.load(fn)     # TODO считать содержимое JSON файла

    gen_exr =  (x['contains_improvement_appeals'] for x in words)    # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())