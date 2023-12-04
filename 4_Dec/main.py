def part1(file):
    sum = 0
    for index, line in enumerate(file):
        split = line.strip("\n").split(": ")
        numbers_sets = split[1].split("|")
        your_numbers = numbers_sets[0].split(" ")
        winning_num = numbers_sets[1].split(" ")
        num_set = set([])
        for num in your_numbers:
            for other_num in winning_num:
                if num == other_num and num != "":
                    num_set.add(num)

        if len(num_set) > 0:
            sum += 2 ** (len(num_set) - 1)

    print(sum)


def part2(file):
    with open("input.txt", "r") as file2:
        copy_scratch = {i: 1 for i in range(len(file2.readlines()))}
    for index, line in enumerate(file):
        print(copy_scratch)
        split = line.strip("\n").split(": ")
        numbers_sets = split[1].split("|")
        your_numbers = numbers_sets[0].split(" ")
        winning_num = numbers_sets[1].split(" ")
        num_set = set([])
        for num in your_numbers:
            for other_num in winning_num:
                if num == other_num and num != "":
                    num_set.add(num)

        if len(num_set) > 0:
            sum += 2 ** (len(num_set) - 1)

        for j in range(len(num_set)):
            copy_scratch[index + 1 + j] += 1 * copy_scratch[index]

    sum = 0
    for num in copy_scratch.values():
        sum += num

    print(sum)


with open("input.txt", "r") as file:
    # part1(file)
    part2(file)
