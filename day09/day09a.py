inputFile = "./input.txt"
exampleInputFile = "./input-example.txt"


class Position:
    def __init__(self, y, x) -> None:
        y = y,
        x = x


def convert_to_vector(split_line):
    direction = split_line[0]
    length = split_line[1]
    if direction == "U":
        return {"y": length, "x": 0}
    elif direction == "D":
        return {"y": -length, "x": 0}
    elif direction == "L":
        return {"y": 0, "x": -length}
    elif direction == "R":
        return {"y": 0, "x": length}


def main():
    with open(inputFile, 'r') as file:
        lines = file.readlines()
    result = 0
    head = Position(0, 0)
    tail = Position(0, 0)
    visited_positions = {}

    for line in lines:
        vector = convert_to_vector(line.split(" "))
        # for

    print(result)


if __name__ == '__main__':
    main()
