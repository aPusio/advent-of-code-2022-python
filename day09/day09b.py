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
        return f"[y:{self.y}, x:{self.x}]"

    def __repr__(self):
        return str(self)


def to_traverse_points(split_line, start_point: Position):
    direction = split_line[0]
    length = int(split_line[1])
    length += 1
    if direction == "U":
        return [Position(i, start_point.x) for i in range(start_point.y + 1, start_point.y + length)]
    elif direction == "D":
        return [Position(i, start_point.x) for i in range(start_point.y - 1, start_point.y - length, -1)]
    elif direction == "L":
        return [Position(start_point.y, i) for i in range(start_point.x - 1, start_point.x - length, -1)]
    elif direction == "R":
        return [Position(start_point.y, i) for i in range(start_point.x + 1, start_point.x + length)]


def get_all_neighbours_and_itself(point: Position):
    return {Position(point.y - 1, point.x - 1),
            Position(point.y - 1, point.x),
            Position(point.y - 1, point.x + 1),
            Position(point.y + 1, point.x - 1),
            Position(point.y + 1, point.x),
            Position(point.y + 1, point.x + 1),
            Position(point.y, point.x - 1),
            Position(point.y, point.x + 1),
            Position(point.y, point.x)}


def get_cross_neighbours(point: Position):
    return {Position(point.y - 1, point.x),
            Position(point.y + 1, point.x),
            Position(point.y, point.x - 1),
            Position(point.y, point.x + 1)}


def get_diagonal_neighbours(point: Position):
    return {Position(point.y - 1, point.x - 1),
            Position(point.y - 1, point.x + 1),
            Position(point.y + 1, point.x - 1),
            Position(point.y + 1, point.x + 1)}


def main():
    with open(inputFile, 'r') as file:
        lines = file.readlines()
    rope = [Position(0, 0)]
    for i in range(0, 9):
        rope.append(Position(0, 0))
    visited_positions = {rope[0]}

    for line in lines:
        print(f'command: {line}')
        traverse_points = to_traverse_points(line.split(" "), rope[0])
        for traverse_point in traverse_points:
            new_rope = rope.copy()
            new_rope[0] = Position(traverse_point.y, traverse_point.x)
            for i in range(1, len(rope)):
                if rope[i] in get_all_neighbours_and_itself(new_rope[i - 1]):
                    print("Tail stays")
                    break
                else:
                    shared_neighbours = get_cross_neighbours(new_rope[i - 1]) & get_all_neighbours_and_itself(rope[i])
                    if shared_neighbours:
                        new_rope[i] = shared_neighbours.pop()
                    else:
                        shared_neighbours = get_diagonal_neighbours(new_rope[i - 1]) & get_all_neighbours_and_itself(rope[i])
                        new_rope[i] = shared_neighbours.pop()
                    if i == 9:
                        visited_positions.add(new_rope[i])
            rope = new_rope
            print(rope)
    print(len(visited_positions))


if __name__ == '__main__':
    main()
