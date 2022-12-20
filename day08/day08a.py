inputFile = "./input.txt"
exampleInputFile = "./input-example.txt"


def main():
    with open(exampleInputFile, 'r') as file:
        lines = file.readlines()
    result = 0
    trees = []
    for i in range(0, len(lines)):
        line = lines[i].strip('\n')
        for char in line:
            row = [eval(i) for i in line]
        trees.append(row)

    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees[0]) - 1):
            print(f'processing {trees[y][x]} y:{y} x:{x}')
            if is_tree_visible(trees, x, y):
                result += 1

    print(trees)
    print(result)


def is_tree_visible(trees, y, x):
    left = trees[y][:x]
    right = trees[y][x+1:]
    up = trees[:y]
    down = trees[y+1:]
    print(f'{left} {right} {up} {down}')
    return True


if __name__ == '__main__':
    main()


