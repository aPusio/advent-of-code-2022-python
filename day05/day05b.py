import re

inputFile = "./input.txt"
exampleInputFile = "./input-example.txt"


if __name__ == '__main__':
    with open(inputFile, 'r') as file:
        lines = file.readlines()

    map_of_stacks = {}
    for line in lines:
        if line == "\n":
            break
        amount_of_stacks = len(line)//4
        for i in range(1, amount_of_stacks+1):
            if not map_of_stacks.get(i):
                map_of_stacks[i] = []
        box_index = 1
        for i in range(1, len(line), 4):
            box_content = line[i]
            if box_content.isalpha() and not box_content.isspace():
                map_of_stacks[box_index].append(box_content)
            box_index += 1
        print(map_of_stacks)

    for line in lines:
        if line.startswith("move"):
            words = line.split(" ")
            amount = int(words[1])
            move_from = int(words[3])
            move_to = int(words[5])
            print(f'{amount} {move_from} {move_to}')

            boxes_to_move = map_of_stacks[move_from][0:amount]
            del map_of_stacks[move_from][0:amount]

            map_of_stacks[move_to] = boxes_to_move + map_of_stacks[move_to]

            print(map_of_stacks)

    result = ""
    for stack in map_of_stacks:
        result += str(map_of_stacks[stack][0])
    print(result)
