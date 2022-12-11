inputFile = "./input.txt"
exampleInputFile = "./input-example.txt"


if __name__ == '__main__':
    with open(inputFile, 'r') as file:
        lines = file.readlines()

    result = 0
    for rucksack in lines:
        first_compartment = set(rucksack[:len(rucksack) // 2])
        second_compartment = set(rucksack[len(rucksack) // 2:-1])
        print(f'{first_compartment} {second_compartment}')
        common_item = (first_compartment & second_compartment).pop()
        if common_item.isupper():
            numeric_common_item = ord(common_item) - ord('A') + 27
        else:
            numeric_common_item = ord(common_item) - ord('a') + 1
        print(f'{common_item} : {numeric_common_item}')
        result += numeric_common_item
    print(result)
