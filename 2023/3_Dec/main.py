#
# symbols = "* $ + #"
#     ints = "1 2 3 4 5 6 7 8 9"
#     grid = []
#     for index, line in enumerate(file):
#         line = line.strip("\n")
#         row = ["."]
#         num = []
#         for charac in line:
#             if charac in ints:
#                 num.append(charac)
#             else:
#                 if len(num) > 0:
#                     number = 0
#                     num_length = len(num)
#                     for j in range(num_length):
#                         number += int(num[j]) * (10 ** (num_length - (j + 1)))
#                     row.append(number)
#                     num = []
#                 row.append(charac)
#         row.append(".")
#         if len(num) > 0:
#             number = 0
#             num_length = len(num)
#             for j in range(num_length):
#                 number += int(num[j]) * (10 ** (num_length - (j + 1)))
#             row.append(number)
#         grid.append(row)
#
#     row = ["." for _ in range(len(grid))]
#     grid.append(row)
#     grid.insert(0, row)
#
#     sum = 0
#     for r_index, row in enumerate(grid):
#         for c_index, entry in enumerate(row):
#             if type(entry) is int:
#                 for i in range(3):
#                     if grid[r_index - 1][c_index - 1 + i] in symbols:
#                         print(entry)
#                         sum += entry
#                         break
#                     elif grid[r_index + 1][c_index - 1 + i] in symbols:
#                         print(entry)
#                         sum += entry
#                         break
#                     elif grid[r_index - 1 + i][c_index - 1] in symbols:
#                         print(entry)
#                         sum += entry
#                         break
#                     elif grid[r_index - 1 + i][c_index + 1] in symbols:
#                         print(entry)
#                         sum += entry
#                         break


def part1(file):
    ints = "0 1 2 3 4 5 6 7 8 9"
    not_important = ints + " ."
    grid = []
    for index, line in enumerate(file):
        line = line.strip("\n")
        row = ["."]
        for charac in line:
            if charac in ints:
                row.append(int(charac))
            else:
                row.append(charac)
        row.append(".")
        grid.append(row)

    row = ["." for _ in range(len(grid) + 1)]
    grid.append(row)
    grid.insert(0, row)

    sum = 0
    for r_index, row in enumerate(grid):
        c_index = 0
        while c_index < len(row):
            if type(row[c_index]) is int:
                # print(row[c_index])
                # print(c_index)
                num_length = 0
                entry = 0
                while type(row[c_index]) is int:
                    entry *= 10
                    entry += row[c_index]
                    num_length += 1
                    c_index += 1

                symbol_found = False

                for j in range(num_length + 2):
                    if not str(grid[r_index - 1][c_index - j]) in not_important:
                        print(entry)
                        sum += entry
                        # print(c_index)
                        c_index -= 1
                        symbol_found = True
                        break
                    elif not str(grid[r_index + 1][c_index - j]) in not_important:
                        print(entry)
                        sum += entry
                        # print(c_index)
                        c_index -= 1
                        symbol_found = True
                        break

                if not symbol_found:
                    for k in range(3):
                        if not str(grid[r_index - 1 + k][c_index - (num_length + 1)]) in not_important:
                            print(entry)
                            sum += entry
                            # print(c_index)
                            c_index -= 1
                            break

                        elif not str(grid[r_index - 1 + k][c_index]) in not_important:
                            print(entry)
                            sum += entry
                            # print(c_index)
                            c_index -= 1
                            break
            c_index += 1
            print(c_index)
    print(sum)
    # print(grid)


def part2(file):
    ints = "0 1 2 3 4 5 6 7 8 9"
    gear_symb = "*"
    grid = []
    for index, line in enumerate(file):
        line = line.strip("\n")
        row = ["."]
        num = []
        for charac in line:
            if charac in ints:
                num.append(charac)
            else:
                if len(num) > 0:
                    number = 0
                    num_length = len(num)
                    for j in range(num_length):
                        number += int(num[j]) * (10 ** (num_length - (j + 1)))
                    for _ in range(num_length):
                        row.append(number)
                    num = []
                row.append(charac)
        row.append(".")
        if len(num) > 0:
            number = 0
            num_length = len(num)
            for j in range(num_length):
                number += int(num[j]) * (10 ** (num_length - (j + 1)))
            for _ in range(num_length):
                row.append(number)
        row.append(".")
        grid.append(row)

    row = ["." for _ in range(len(grid[0]))]
    grid.append(row)
    grid.insert(0, row)

    for row in grid:
        print(row)

    sum = 0
    gear_combos = []
    for i, row in enumerate(grid):
        for j, entry in enumerate(row):
            num_around = set([])
            if entry == gear_symb:

                # Check row above and below
                # print(f"{i}, {j}")
                for k in range(3):
                    # print(f"{i + 1}, {j + k - 1}")
                    if type(grid[i - 1][j + k - 1]) is int:
                        num_around.add(grid[i - 1][j + k - 1])
                    if type(grid[i + 1][j + k - 1]) is int:
                        num_around.add(grid[i + 1][j + k - 1])

                if type(grid[i][j - 1]) is int:
                    num_around.add(grid[i][j - 1])
                if type(grid[i][j + 1]) is int:
                    num_around.add(grid[i][j + 1])

                if len(num_around) == 2:
                    # print(num_around)
                    gear_combos.append(num_around)
    set_of_combo = [list(gear_combos[0])]
    for i, combo in enumerate(gear_combos):
        combo_list = list(combo)
        in_set = False
        for other_combo in set_of_combo:
            if (combo_list[0] == other_combo[0] and combo_list[1] == other_combo[1]) or \
                    (combo_list[1] == other_combo[0] and combo_list[1] == other_combo[0]):
                in_set = True
                break
        if not in_set:
            set_of_combo.append(combo_list)

    print(set_of_combo)
    for l in gear_combos:
        mult = 1
        for num in l:
            mult *= num
        sum += mult

    print(sum)
    # print(grid)

def attempt_two(file):
    ints = "0 1 2 3 4 5 6 7 8 9"
    gear_symb = "*"
    grid = []
    for index, line in enumerate(file):
        line = line.strip("\n")
        row = ["."]
        for charac in line:
            if charac in ints:
                row.append(int(charac))
            else:
                row.append(charac)
        row.append(".")
        grid.append(row)

    row = ["." for _ in range(len(grid) + 1)]
    grid.append(row)
    grid.insert(0, row)

    for row in grid:
        print(row)

    sum = 0
    gear_combos = []
    for i, row in enumerate(grid):
        for j, entry in enumerate(row):
            num_around = set([])
            if entry == gear_symb:
                for k in range(3):
                    # print(f"{i + 1}, {j + k - 1}")
                    if type(grid[i - 1][j + k - 1]) is int:
                        temp_i, temp_k = i - 1, j + k - 1
                        while type(grid[temp_i][temp_k]) is int:
                            temp_k -= 1

                        temp_k += 1
                        number = 0
                        while type(grid[temp_i][temp_k]) is int:
                            number *= 10
                            number += grid[temp_i][temp_k]
                            temp_k += 1

                        num_around.add(number)
                    if type(grid[i + 1][j + k - 1]) is int:
                        temp_i, temp_k = i + 1, j + k - 1
                        while type(grid[temp_i][temp_k]) is int:
                            temp_k -= 1

                        temp_k += 1
                        number = 0
                        while type(grid[temp_i][temp_k]) is int:
                            number *= 10
                            number += grid[temp_i][temp_k]
                            temp_k += 1

                        num_around.add(number)

                if type(grid[i][j - 1]) is int:
                    temp_i, temp_k = i, j - 1
                    while type(grid[temp_i][temp_k]) is int:
                        temp_k -= 1

                    temp_k += 1
                    number = 0
                    while type(grid[temp_i][temp_k]) is int:
                        number *= 10
                        number += grid[temp_i][temp_k]
                        temp_k += 1

                    num_around.add(number)
                if type(grid[i][j + 1]) is int:
                    temp_i, temp_k = i, j + 1
                    while type(grid[temp_i][temp_k]) is int:
                        temp_k -= 1

                    temp_k += 1
                    number = 0
                    while type(grid[temp_i][temp_k]) is int:
                        number *= 10
                        number += grid[temp_i][temp_k]
                        temp_k += 1

                    num_around.add(number)

                if len(num_around) == 2:
                    # print(num_around)
                    gear_combos.append(num_around)

    set_of_combo = [list(gear_combos[0])]
    for i, combo in enumerate(gear_combos):
        combo_list = list(combo)
        in_set = False
        for other_combo in set_of_combo:
            if (combo_list[0] == other_combo[0] and combo_list[1] == other_combo[1]) or \
                    (combo_list[1] == other_combo[0] and combo_list[1] == other_combo[0]):
                in_set = True
                break
        if not in_set:
            set_of_combo.append(combo_list)

    print(set_of_combo)
    for l in gear_combos:
        mult = 1
        for num in l:
            mult *= num
        sum += mult

    print(sum)

with open("input.txt", "r") as file:
    # part1(file)
    # part2(file)
    attempt_two(file)
