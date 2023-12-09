ints = [str(i) for i in range(1, 10)]
words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
dictionary = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def get_line_val(line):
    current_val = []
    for index, letter in enumerate(line):
        # print(letter)
        for word in ints:
            if letter == word:
                current_val.append(int(int(letter)))

    if len(current_val) == 1:
        return current_val[0] * 10 + current_val[0]
    else:
        return current_val[0] * 10 + current_val[-1]


def part1(file):
    sum = 0
    for line in file:
        sum += get_line_val(line.strip("\n"))
    return sum

def part2(file):
    sum = 0
    for index, line in enumerate(file):
        current_line = line.strip("\n")
        i = 0
        while i < len(current_line):
            for word in words:
                letters = ""
                x = 0
                while i + x < len(current_line) and x < len(word) and current_line[i + x] == word[x]:
                    letters += current_line[i + x]
                    x += 1
                if letters == word:
                    current_line = current_line[:i] + str(dictionary.get(word)) + current_line[i + 1:]
                    break
            i += 1

        for line in file:
            sum += get_line_val(line.strip("\n"))

    return sum


with open("input.txt", "r") as file:
    # words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    # dictionary = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    # print(ints)
    # for index, line in enumerate(file):
    #     val = 0
    #     current_val = []
    #     current_line = line.strip("\n")
    #     i = 0
    #     while i < len(current_line):
    #         # print(f"index: {i}")
    #         # print(f"letter: {current_line[i]}")
    #         for word in words:
    #             letters = ""
    #             x = 0
    #             while i + x < len(current_line) and x < len(word) and current_line[i + x] == word[x]:
    #                 letters += current_line[i + x]
    #                 x += 1
    #             if letters == word:
    #                 # print(current_line)
    #                 # print(i)
    #                 current_line = current_line[:i] + str(dictionary.get(word)) + current_line[i + 1:]
    #                 # print(f"word: {word}")
    #                 break
    #         i += 1
    #
    #     # print()
    #     # print("qweqwer")
    #     # print(current_line)
    #     current_val = []
    #     for i, letter in enumerate(current_line.strip("\n")):
    #         # print(letter)
    #         for word in ints:
    #             if letter == word:
    #                 current_val.append(int(int(letter)))
    #
    #     if len(current_val) == 1:
    #         val = current_val[0] * 10 + current_val[0]
    #     else:
    #         val = current_val[0] * 10 + current_val[-1]
    #
    #     sum += val
    #     print(f"val: {val}")
    #     print(f"sum{sum}")

    print(part1(file))
if __name__ == "__main__":
    print('qwer')
