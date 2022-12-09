inputFile = "./input.txt"
exampleInputFile = "./input-example.txt"

if __name__ == '__main__':
    with open(inputFile, 'r') as file:
        lines = file.readlines()

    sums = []
    current_sum = 0
    for line in lines:
        if line.strip():
            number = int(line)
            print(number)
            current_sum += number
        else:
            sums.append(current_sum)
            current_sum = 0
            print("empty line")
    sums.sort(reverse=True)
    print(sum(sums[:3]))
