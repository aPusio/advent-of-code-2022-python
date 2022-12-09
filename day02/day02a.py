inputFile = "./input.txt"
exampleInputFile = "./input-example.txt"


class Figure:
    value = 0
    beats = ""

    def __init__(self, value, beats):
        self.value = value
        self.beats = beats


rules = {
    "A": Figure(1, "C"),  # rock
    "B": Figure(2, "A"),  # paper
    "C": Figure(3, "B")  # scissors
}

if __name__ == '__main__':
    with open(inputFile, 'r') as file:
        lines = file.readlines()

    result = 0
    for line in lines:
        split = line.split()
        opponent = split[0]
        response = split[1].replace("Y", "B").replace("X", "A").replace("Z", "C")
        print(opponent + " AND " + response)
        if opponent == response:
            result += 3 + rules.get(response).value
        elif rules.get(response).beats == opponent:
            result += 6 + rules.get(response).value
        else:
            result += rules.get(response).value
    print(result)
