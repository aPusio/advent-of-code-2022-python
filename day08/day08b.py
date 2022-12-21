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
            all_visible = count_all_visible_trees(trees, x, y)
            print(f'visible trees: {all_visible}')
            if result < all_visible:
                result = all_visible

    print(trees)
    print(result)


def count_visible_trees(visible_trees, tree):
    count = 0
    for visible_tree in visible_trees:
        count += 1
        if visible_tree >= tree:
            break
    return count


def count_all_visible_trees(trees, y, x):
    tree = trees[y][x]
    left = trees[y][:x]
    left.reverse()
    right = trees[y][x+1:]
    col = column(trees, x)
    up = col[:y]
    up.reverse()
    down = col[y+1:]
    # print(f'{left} {right} {up} {down}')

    return count_visible_trees(left, tree) * \
        count_visible_trees(right, tree) * \
        count_visible_trees(up, tree) * \
        count_visible_trees(down, tree)


def column(matrix, i):
    return [row[i] for row in matrix]


if __name__ == '__main__':
    main()


