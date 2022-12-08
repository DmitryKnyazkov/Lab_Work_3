import json


def task(input_filename: str, output_filename: str) -> None:
    with open(input_filename, "r", encoding="utf-8") as i_f:
        with open(output_filename, "w", encoding='utf-8') as o_f:
            str_ = json.load(i_f)
            json.dump(str_, o_f, indent=4)





  # TODO считать содержимое json файл input.json

    # TODO записать содержимое в json файл output.json с отступами


if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")
