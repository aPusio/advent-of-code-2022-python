inputFile = "./input.txt"
exampleInputFile = "./input-example.txt"


def main():
    with open(inputFile, 'r') as file:
        lines = file.readlines()
    result = 0
    # because addition is after the cycle
    queue = [None]
    for line in lines:
        if line.startswith("addx"):
            value = int(line.removeprefix("addx "))
            queue.append(None)
            queue.append(value)
        else:
            queue.append(None)
    crt = [" " for _ in range(0, 240)]
    register = 1
    for cycle in range(0, len(queue)):
        if queue[cycle]:
            register += queue[cycle]
        if abs((cycle % 40) - register) <= 1:
            crt[cycle] = "#"
    print_crt(crt)
    print(result)


def print_crt(crt):
    for i in range(0, len(crt)):
        print(crt[i], end="")
        if (i + 1) % 40 == 0:
            print()


if __name__ == '__main__':
    main()
