inputFile = "./input.txt"
exampleInputFile = "./input-example.txt"


if __name__ == '__main__':
    with open(inputFile, 'r') as file:
        lines = file.readlines()

    result = 0
    batch_size = 3
    # https://blog.finxter.com/how-to-loop-through-a-python-list-in-batches/
    for i in range(0, len(lines) - batch_size + 1, batch_size):
        batch = lines[i: i+batch_size]
        first_line = set(batch[0][:-1])
        second_line = set(batch[1][:-1])
        third_line = set(batch[2][:-1])
        common_item = (first_line & second_line & third_line).pop()
        if common_item.isupper():
            numeric_common_item = ord(common_item) - ord('A') + 27
        else:
            numeric_common_item = ord(common_item) - ord('a') + 1
        print(f'{common_item} : {numeric_common_item}')
        result += numeric_common_item
    print(result)
