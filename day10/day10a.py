inputFile = "./input.txt"
exampleInputFile = "./input-example.txt"


def main():
    with open(exampleInputFile, 'r') as file:
        lines = file.readlines()
    result = 0
    # buffer = [1]
    cycle = 0
    for line in lines:
        if line.startswith("addx"):
            
            value = int(line.removeprefix("addx "))
            cycle += 1
            print(f'add: {value}')
        else:
            cycle += 1
            print("noop")

    print(result)


if __name__ == '__main__':
    main()
