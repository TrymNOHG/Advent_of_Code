def is_move_valid(current_index, next_index, pipe_type):
    x, y = current_index
    x_2, y_2 = next_index
    if x_2 - x > 0:  # From the left
        if pipe_type == '-':
            return True, (x + 2, y), 0  # Next index + rotation
        elif pipe_type == '7':
            return True, (x + 1, y + 1), -90
        elif pipe_type == 'J':
            return True, (x + 1, y - 1), 90
        else:
            return False, (), 0
    elif x_2 - x < 0:  # From the right
        if pipe_type == '-':
            return True, (x - 2, y), 0  # Next index
        elif pipe_type == 'L':
            return True, (x - 1, y - 1), -90
        elif pipe_type == 'F':
            return True, (x - 1, y + 1), 90
        else:
            return False, (), 0
    elif y_2 - y > 0:  # From above
        if pipe_type == '|':
            return True, (x, y + 2), 0  # Next index
        elif pipe_type == 'J':
            return True, (x - 1, y + 1), -90
        elif pipe_type == 'L':
            return True, (x + 1, y + 1), 90
        else:
            return False, (), 0
    else:  # y_2 - y > 0  From below
        if pipe_type == '|':
            return True, (x, y - 2), 0  # Next index
        elif pipe_type == '7':
            return True, (x - 1, y - 1), 90
        elif pipe_type == 'F':
            return True, (x + 1, y - 1), -90
        else:
            return False, (), 0


def part1(file):
    grid = [[entry for entry in line.strip("\n")] for line in file]
    starting_pos = ()
    for i, row in enumerate(grid):
        for j, entry in enumerate(row):
            if entry == 'S':
                starting_pos = (j, i)

    indexed_grid_map = [[10000000 for _ in row] for row in grid]

    valid_start_dir = []

    left_move = (starting_pos[0] - 1, starting_pos[1])
    down_move = (starting_pos[0], starting_pos[1] + 1)
    right_move = (starting_pos[0] + 1, starting_pos[1])
    up_move = (starting_pos[0], starting_pos[1] - 1)

    starting_moves = [left_move, down_move, right_move, up_move]
    for move in starting_moves:
        is_valid_move, _, _ = is_move_valid(starting_pos, move, grid[move[1]][move[0]])
        if is_valid_move:
            valid_start_dir.append(move)  # Contains next index and the direction of pipe

    for start_pipe_coords in valid_start_dir:
        current = starting_pos
        next_move = start_pipe_coords
        next_pipe = grid[start_pipe_coords[1]][start_pipe_coords[0]]
        i = 0
        while next_pipe != 'S':
            _, start_pipe_coords, _ = is_move_valid(current, next_move, next_pipe)
            prev = current
            current = next_move
            next_move = start_pipe_coords
            next_pipe = grid[next_move[1]][next_move[0]]

            indexed_grid_map[prev[1]][prev[0]] = min(indexed_grid_map[prev[1]][prev[0]], i)

            i += 1

    max_val = 0
    for i, row in enumerate(indexed_grid_map):
        print(row)
        for j, entry in enumerate(row):
            if not entry == 10000000:
                max_val = max(max_val, entry)

    print(max_val)


def part2(file):
    grid = [[entry for entry in line.strip("\n")] for line in file]
    starting_pos = ()
    for i, row in enumerate(grid):
        for j, entry in enumerate(row):
            if entry == 'S':
                starting_pos = (j, i)

    indexed_grid_map = [['.' for _ in row] for row in grid]
    direction_map = {0: '>', 90: '^', 180: '<', 270: 'v'}

    valid_start_dir = []

    left_move = [(starting_pos[0] - 1, starting_pos[1]), 270]
    down_move = [(starting_pos[0], starting_pos[1] + 1), 180]
    right_move = [(starting_pos[0] + 1, starting_pos[1]), 90]
    up_move = [(starting_pos[0], starting_pos[1] - 1), 0]

    starting_moves = [left_move, down_move, right_move, up_move]
    for move in starting_moves:
        is_valid_move, _, _ = is_move_valid(starting_pos, move[0], grid[move[0][1]][move[0][0]])
        if is_valid_move:
            valid_start_dir = move  # Contains next index and the direction of pipe
            break

    current = starting_pos
    next_move = valid_start_dir[0]
    next_pipe = grid[valid_start_dir[0][1]][valid_start_dir[0][0]]
    rotation = valid_start_dir[1]
    i = 0

    indexed_grid_map[next_move[1]][next_move[0]] = [rotation]

    while next_pipe != 'S':
        _, start_pipe_coords, new_rotation = is_move_valid(current, next_move, next_pipe)
        current = next_move
        next_move = start_pipe_coords
        old_rotation = rotation
        next_pipe = grid[next_move[1]][next_move[0]]
        rotation = (rotation + new_rotation) % 360
        indexed_grid_map[current[1]][current[0]] = [old_rotation, rotation]
        if next_pipe == 'S':
            indexed_grid_map[next_move[1]][next_move[0]] = [rotation, valid_start_dir[1]]
            break

        i += 1

    sum_of_non_pipe = 0
    for i, row in enumerate(indexed_grid_map):
        for j, entry in enumerate(row):
            if entry == '.':
                sum_of_non_pipe += 1

    area = 0

    for i, row in enumerate(indexed_grid_map):
        previous_num = [-1]
        for j, entry in enumerate(row):
            if entry == '.':
                is_in = False
                # Check left first
                if j > 0 and 0 in previous_num:
                    is_in = True

                # Find right pipe
                if not is_in and j < len(row) - 1:
                    right_pip = row[j + 1]
                    index = 0
                    while (j + 1 + index) < len(row) - 1 and right_pip == '':
                        index += 1
                        right_pip = row[j + 1 + index]

                    if type(right_pip) == list and 180 in right_pip == 180:
                        is_in = True

                # Check above
                if not is_in and i > 0:
                    above_pipe = indexed_grid_map[i - 1][j]
                    index = 0
                    while (i - 1 - index) > 0 and above_pipe == '':
                        index += 1
                        above_pipe = indexed_grid_map[i - 1 - index][j]
                    if above_pipe == 270:
                        is_in = True

                # Check below pipe
                if not is_in and i < len(indexed_grid_map) - 1:
                    below_pipe = indexed_grid_map[i + 1][j]
                    index = 0
                    while (i + 1 + index) < len(indexed_grid_map) - 1 and below_pipe == '':
                        index += 1
                        below_pipe = indexed_grid_map[i + 1 + index][j]
                    if below_pipe == 90:
                        is_in = True

                if is_in:
                    area += 1
                    indexed_grid_map[i][j] = 'I'
            else:
                previous_num = entry

    for row in indexed_grid_map:
        print(row)

    print(area)


with open("input.txt", "r") as file:
    # part1(file)
    part2(file)
