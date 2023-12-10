def is_move_valid(current_index, next_index, pipe_type):
    x, y = current_index
    x_2, y_2 = next_index
    if x_2 - x > 0:  # To the left
        if pipe_type == '-':
            return True, (x + 2, y)  # Next index
        elif pipe_type == '7':
            return True, (x + 1, y + 1)
        elif pipe_type == 'J':
            return True, (x + 1, y - 1)
        else:
            return False, ()
    elif x_2 - x < 0:  # To the right
        if pipe_type == '-':
            return True, (x - 2, y)  # Next index
        elif pipe_type == 'L':
            return True, (x - 1, y - 1)
        elif pipe_type == 'F':
            return True, (x - 1, y + 1)
        else:
            return False, ()
    elif y_2 - y > 0:  # Below
        if pipe_type == '|':
            return True, (x, y + 2)  # Next index
        elif pipe_type == 'J':
            return True, (x - 1, y + 1)
        elif pipe_type == 'L':
            return True, (x + 1, y + 1)
        else:
            return False, ()
    else:  # y_2 - y > 0  Above
        if pipe_type == '|':
            return True, (x, y - 2)  # Next index
        elif pipe_type == '7':
            return True, (x - 1, y - 1)
        elif pipe_type == 'F':
            return True, (x + 1, y - 1)
        else:
            return False, ()


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

    print(starting_pos)

    # grid [y] [x]
    print(grid[0][2])

    starting_moves = [left_move, down_move, right_move, up_move]
    for move in starting_moves:
        # print(move)
        # print(grid[move[1]])
        # print(grid[move[1]][move[0]])
        is_valid_move, _ = is_move_valid(starting_pos, move, grid[move[1]][move[0]])
        if is_valid_move:
            valid_start_dir.append(move)  # Contains next index and the direction of pipe


    print(valid_start_dir)

    for start_pipe_coords in valid_start_dir:
        current = starting_pos
        next_move = start_pipe_coords
        next_pipe = grid[start_pipe_coords[1]][start_pipe_coords[0]]
        i = 0
        while next_pipe != 'S':
            _, start_pipe_coords = is_move_valid(current, next_move, next_pipe)
            print(current)
            print(next_move)
            print(start_pipe_coords)
            # print(_)
            # print(start_pipe_coords)
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
    for index, line in enumerate(file):
        print(line)


with open("input.txt", "r") as file:
    part1(file)
    # part2(file)
