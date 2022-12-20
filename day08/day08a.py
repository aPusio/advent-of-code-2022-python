inputFile = "./input.txt"
exampleInputFile = "./input-example.txt"


def main():
    with open(inputFile, 'r') as file:
        lines = file.readlines()
    result = 0
    trees = []
    for i in range(0, len(lines)):
        line = lines[i].strip('\n')
        row = [eval(i) for i in line]
        trees.append(row)

    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees[0]) - 1):
            print(f'processing {trees[y][x]} y:{y} x:{x}')
            if is_tree_visible(trees, x, y):
                print("VISIBLE")
                result += 1

    print(trees)
    print(result + len(trees[0]) * 2 + len(trees) * 2 - 4)


def is_tree_visible(trees, y, x):
    tree = trees[y][x]
    left = trees[y][:x]
    right = trees[y][x+1:]
    col = column(trees, x)
    up = col[:y]
    down = col[y+1:]
    # print(f'{left} {right} {up} {down}')
    return len([i for i in left if i >= tree]) == 0 or \
        len([i for i in right if i >= tree]) == 0 or \
        len([i for i in up if i >= tree]) == 0 or \
        len([i for i in down if i >= tree]) == 0


def column(matrix, i):
    return [row[i] for row in matrix]


if __name__ == '__main__':
    main()


