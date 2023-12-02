def get_dict_large(file):
    dict = {}
    colors = ["blue", "red", "green"]
    for index, line in enumerate(file):
        game, sets = line.strip("\n").split(":")
        sets = sets.split(";")
        dict[game[game.index("Game "):]] = {"blue": 0, "red": 0, "green": 0}
        for set in sets:
            individ_set = set.split(",")
            for entry in individ_set:
                splitage = entry.split(" ")
                # print(splitage)
                value = int(splitage[1])
                if dict[game[game.index("Game "):]][splitage[2]] < value:
                    dict[game[game.index("Game "):]][splitage[2]] = value
    return dict

def get_dict_small(file):
    dict = {}
    colors = ["blue", "red", "green"]
    for index, line in enumerate(file):
        game, sets = line.strip("\n").split(":")
        sets = sets.split(";")
        dict[game[game.index("Game "):]] = {"blue": -1, "red": -1, "green": -1}
        for set in sets:
            individ_set = set.split(",")
            for entry in individ_set:
                splitage = entry.split(" ")
                # print(splitage)
                value = int(splitage[1])
                if dict[game[game.index("Game "):]][splitage[2]] > value or dict[game[game.index("Game "):]][splitage[2]] == -1:
                    dict[game[game.index("Game "):]][splitage[2]] = value
    return dict

def get_legal_sets(dict, red, green, blue):
    sum = 0
    print(dict)
    for entry in dict:
        print(entry)
        game = entry
        entry = dict[entry]
        if entry["red"] <= red and entry["green"] <= green and entry["blue"] <= blue:
            sum += int(game.split(" ")[1])
    print(sum)
def part1(file):
    dict = get_dict_large(file)
    get_legal_sets(dict, 12, 13, 14)


def part2(file):
    dict = get_dict_large(file)
    sum = 0
    print(dict)
    for entry in dict:
        print(entry)
        game = entry
        entry = dict[entry]
        print(entry)
        sum += entry["red"] * entry["green"] * entry["blue"]
    print(sum)


with open("input.txt", "r") as file:
    # part1(file)
    part2(file)

if __name__ == "__main__":
    print('qwer')
