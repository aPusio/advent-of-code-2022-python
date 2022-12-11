inputFile = "./input.txt"
exampleInputFile = "./input-example.txt"


class Figure:
    value = 0
    beats = ""
    lose = ""

    def __init__(self, value, beats, lose):
        self.value = value
        self.beats = beats
        self.lose = lose


rules = {
    "A": Figure(1, "C", "B"),  # rock
    "B": Figure(2, "A", "C"),  # paper
    "C": Figure(3, "B", "A")  # scissors
}

if __name__ == '__main__':
    with open(inputFile, 'r') as file:
        lines = file.readlines()

    result = 0
    for line in lines:
        split = line.split()
        opponent = split[0]
        match_result = split[1]
        print(opponent + " AND " + match_result)
        response = ""
        if match_result == "Y":
            response = opponent
        elif match_result == "X":
            response = rules.get(opponent).beats
        else:
            response = rules.get(opponent).lose

        if opponent == response:
            print("draw")
            result += 3 + rules.get(response).value
        elif rules.get(response).beats == opponent:
            print("win")
            result += 6 + rules.get(response).value
        else:
            print("lose")
            result += rules.get(response).value
    print(result)
