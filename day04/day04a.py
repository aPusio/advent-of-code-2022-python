import re

inputFile = "./input.txt"
exampleInputFile = "./input-example.txt"


if __name__ == '__main__':
    with open(inputFile, 'r') as file:
        lines = file.readlines()

    result = 0
    for sectionString in lines:
        split = re.split("-|,|\n", sectionString)
        first_range = set(range(int(split[0]), int(split[1])+1))
        second_range = set(range(int(split[2]), int(split[3])+1))
        print(f'{first_range} {second_range}')
        if first_range.issuperset(second_range) or second_range.issuperset(first_range):
            result += 1
    print(result)
