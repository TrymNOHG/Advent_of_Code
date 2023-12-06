# Would be cool to look into interval tree implementation to solve this
import time

def part1(file):
    seeds = file.readline().strip("\n").split(":")[-1].split(" ")[1:]

    file.readline()
    maps = {}
    current_map = ""
    for index, line in enumerate(file):
        if ":" in line:
            current_map = line.strip(":\n")
            maps[current_map] = []
        else:
            maps[current_map].append(line.strip("\n").split(" "))
    print(maps)
    #
    seed_vals = []
    for seed in seeds:
        seed_val = int(seed)
        seed_map_val = [seed_val]
        for map in maps.values():
            added = False
            for ranges in map:
                if len(ranges) == 1:
                    break
                if 0 <= seed_val - int(ranges[1]) <= int(ranges[2]):
                    seed_val = (seed_val - int(ranges[1]) + int(ranges[0]))
                    seed_map_val.append(seed_val)
                    added = True
                    break
            if not added:
                seed_map_val.append(seed_val)
        # arent mapped then same dest num
        seed_vals.append(seed_map_val)
    print(seed_vals)

    lowest_loc = 100000000
    for mapped_vals in seed_vals:
        lowest_loc = min(mapped_vals[-1], lowest_loc)

    print(lowest_loc)

def part2(file):
    seeds = file.readline().strip("\n").split(":")[-1].split(" ")[1:]

    file.readline()
    maps = {}
    current_map = ""
    for index, line in enumerate(file):
        if ":" in line:
            current_map = line.strip(":\n")
            maps[current_map] = []
        else:
            maps[current_map].append(line.strip("\n").split(" "))
    #
    index = 0
    mapped_bins = []
    while index < len(seeds):
        source_values = [[int(seeds[index]), int(seeds[index + 1])]]  # seed_val, seed_range
        map_bins = {}
        for map_name in maps:
            map_val = maps[map_name]
            new_source_val = []
            for value in source_values:
                # print(value)

                not_mapped = [value]
                for ranges in map_val:
                    if len(ranges) == 1:
                        break

                    temp_not_mapped = not_mapped
                    not_mapped = []
                    for entry in temp_not_mapped:
                        source_begin = entry[-2]
                        source_end = source_begin + entry[-1]

                        dest_begin = int(ranges[1])
                        dest_end = int(ranges[2]) + dest_begin

                        map_start = int(ranges[0])

                        diff_begin = source_begin - dest_begin

                        if source_end < dest_begin or source_begin > dest_end:
                            not_mapped.append([source_begin, source_end - source_begin])
                        else:
                            if diff_begin < 0:
                                not_mapped.append([source_begin, source_begin - dest_begin])
                                new_source_val.append([map_start, min(dest_end, source_end) - dest_begin])
                            else:
                                new_source_val.append([map_start + (source_begin - dest_begin), min(dest_end, source_end) - source_begin])

                            if dest_end < source_end:
                                not_mapped.append([dest_end, source_end - dest_end])

                if len(not_mapped) > 0:
                    new_source_val += not_mapped
                source_values = new_source_val
            map_bins[map_name] = new_source_val

        print(mapped_bins)
        mapped_bins.append(map_bins["humidity-to-location map"])
        index += 2
    # print(seed_vals)
    print(mapped_bins)
    lowest_loc = 100000000
    mapped_vals = []
    for seed_stem in mapped_bins:
        for loc in seed_stem:
            mapped_vals.append(loc[:][0])

    # print(mapped_vals)
    for mapped_val in mapped_vals:
        lowest_loc = min(mapped_val, lowest_loc)

    print(lowest_loc)


with open("input.txt", "r") as file:
    # part1(file)
    start_time = time.time_ns()
    part2(file)
    stop_time = time.time_ns()
    print((stop_time-start_time)/10**6)
