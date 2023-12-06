def part1(file):
    text = file.readlines()
    time_field = text[0].strip("\n").split(":")
    distance_field = text[1].strip("\n").split(":")

    durations = time_field[1].split(" ")
    best_dist = distance_field[1].split(" ")

    dist_index = 0
    pairs = []
    for duration in durations:
        if duration != "":
            while best_dist[dist_index] == "":
                dist_index += 1

            pairs.append([duration, best_dist[dist_index]])
            dist_index += 1

    num_valid_way = [0 for _ in range(len(pairs))]
    for index, race in enumerate(pairs):
        time_spent = 0
        duration = int(race[0])
        while time_spent <= duration:
            distance = (duration - time_spent) * time_spent
            if distance > int(race[1]):
                num_valid_way[index] += 1
            time_spent += 1

    print(num_valid_way)
    mult = 1
    for way in num_valid_way:
        mult *= way

    print(mult)



def part2(file):
    text = file.readlines()
    time_field = text[0].strip("\n").split(":")
    distance_field = text[1].strip("\n").split(":")

    duration = int(time_field[1].replace(" ", ""))
    best_dist = int(distance_field[1].replace(" ", ""))

    num_valid_way = 0
    time_spent = 0
    while time_spent <= duration:
        distance = (duration - time_spent) * time_spent
        if distance > best_dist:
            num_valid_way = (duration - time_spent) - time_spent + 1
            break
        time_spent += 1

    print(num_valid_way)

with open("input.txt", "r") as file:
    # part1(file)
    part2(file)
