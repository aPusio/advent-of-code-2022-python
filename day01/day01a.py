inputFile = "./input.txt"
exampleInputFile = "./input-example.txt"

if __name__ == '__main__':
    with open(inputFile, 'r') as file:
        lines = file.readlines()

    max_sum = 0
    current_sum = 0
    for line in lines:
        if line.strip():
            number = int(line)
            print(number)
            current_sum += number
        else:
            if current_sum > max_sum:
                max_sum = current_sum
            current_sum = 0
            print("empty line")
    print(max_sum)
