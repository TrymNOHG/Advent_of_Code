def part1(file):
    extrapolated_val_sum = 0
    for index, line in enumerate(file):
        sequence = [line.strip("\n").split(" ")]
        all_zeros = False
        while not all_zeros:
            all_zeros = True
            new_sequence = []

            for i in range(len(sequence[-1]) - 1):
                diff = int(sequence[-1][i+1]) - int(sequence[-1][i])
                if diff != 0:
                    all_zeros = False
                new_sequence.append(diff)
            sequence.append(new_sequence)

        sequence[-1].append(0)
        for j in range(len(sequence) - 2, -1, -1):
            extrapolated_val = int(sequence[j][-1]) + int(sequence[j+1][-1])
            sequence[j].append(extrapolated_val)

        extrapolated_val_sum += int(sequence[0][-1])
        print(sequence)

    print(extrapolated_val_sum)


def part2(file):
    extrapolated_val_sum = 0
    for index, line in enumerate(file):
        sequence = [line.strip("\n").split(" ")]
        all_zeros = False
        while not all_zeros:
            all_zeros = True
            new_sequence = []

            for i in range(len(sequence[-1]) - 1):
                diff = int(sequence[-1][i + 1]) - int(sequence[-1][i])
                if diff != 0:
                    all_zeros = False
                new_sequence.append(diff)
            sequence.append(new_sequence)

        sequence[-1].insert(0, 0)
        for j in range(len(sequence) - 2, -1, -1):
            extrapolated_val = int(sequence[j][0]) - int(sequence[j + 1][0])
            print(extrapolated_val)
            sequence[j].insert(0, extrapolated_val)

        extrapolated_val_sum += int(sequence[0][0])
        print(sequence)

    print(extrapolated_val_sum)


with open("input.txt", "r") as file:
    # part1(file)
    part2(file)
