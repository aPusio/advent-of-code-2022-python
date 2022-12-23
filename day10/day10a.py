inputFile = "./input.txt"
exampleInputFile = "./input-example.txt"


def main():
    with open(inputFile, 'r') as file:
        lines = file.readlines()
    result = 0
    # first - because count starts from 1, second - because addition is after the cycle
    queue = [None, None]
    for line in lines:
        if line.startswith("addx"):
            value = int(line.removeprefix("addx "))
            queue.append(None)
            queue.append(value)
        else:
            queue.append(None)
    checkpoints = [i for i in range(20, len(queue), 40)]
    register = 1
    for i in range(0, len(queue)):
        if queue[i]:
            register += queue[i]
        if i in checkpoints:
            print(f'Checkpoint! {i}*{register}={i * register}')
            result += i * register

    print(register)
    print(result)


if __name__ == '__main__':
    main()
