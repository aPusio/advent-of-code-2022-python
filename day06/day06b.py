import re

inputFile = "./input.txt"
exampleInputFile = "./input-example.txt"


if __name__ == '__main__':
    with open(inputFile, 'r') as file:
        lines = file.readlines()

    result = 0
    line = lines[0]
    window_size = 14
    for i in range(len(line) - window_size + 1):
        batch = line[i:i + window_size]
        if len(set(batch)) == len(batch):
            print(f'result: {i+window_size}')
            break

    print(result)
