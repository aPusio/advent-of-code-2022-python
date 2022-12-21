inputFile = "./input.txt"
exampleInputFile = "./input-example.txt"


class Position:
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"y:{self.y}, x:{self.x}"


def to_traverse_points(split_line, start_point: Position):
    direction = split_line[0]
    length = int(split_line[1])
    length += 1
    if direction == "U":
        return [Position(i, start_point.x) for i in range(start_point.y+1, start_point.y + length)]
    elif direction == "D":
        return [Position(i, start_point.x) for i in range(start_point.y-1, start_point.y - length, -1)]
    elif direction == "L":
        return [Position(start_point.y, i) for i in range(start_point.x-1, start_point.x - length, -1)]
    elif direction == "R":
        return [Position(start_point.y, i) for i in range(start_point.x+1, start_point.x + length)]


def get_neighbours_and_itself(head: Position):
    return [Position(head.y - 1, head.x - 1),
            Position(head.y - 1, head.x),
            Position(head.y - 1, head.x + 1),
            Position(head.y + 1, head.x - 1),
            Position(head.y + 1, head.x),
            Position(head.y + 1, head.x + 1),
            Position(head.y, head.x - 1),
            Position(head.y, head.x + 1),
            Position(head.y, head.x)]


def main():
    with open(inputFile, 'r') as file:
        lines = file.readlines()
    head = Position(0, 0)
    tail = Position(0, 0)
    visited_positions = {tail}

    for line in lines:
        print(f'command: {line}')
        traverse_points = to_traverse_points(line.split(" "), head)
        for traverse_point in traverse_points:
            moved_head = Position(traverse_point.y, traverse_point.x)
            print(f'head moved to: {moved_head}')
            head_neighbours = get_neighbours_and_itself(moved_head)
            if tail in head_neighbours:
                print("Tail stays")
            else:
                tail = head
                visited_positions.add(tail)
                print(f'Tail moves {tail}')
            head = moved_head
        # print(traverse_points)
    print(len(visited_positions))


if __name__ == '__main__':
    main()
