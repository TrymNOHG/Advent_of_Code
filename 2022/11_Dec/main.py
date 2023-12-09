from tqdm import tqdm
import math

# Parsing the data for each monkey
with open("input.txt", "r") as notes:
    monkey_info = {}
    monkey = ""
    for info in notes:
        if "Monkey" in info:
            monkey = info.strip("\n").lower()
            monkey_info[monkey] = {}
            monkey_info[monkey]["Num inspections"] = 0
        else:
            info_split = info.strip("\n").strip(" ").split(":")
            if info_split[0] == "Starting items":
                monkey_info[monkey][info_split[0]] = info_split[1].strip(" ").split(",")
                continue
            if len(info_split) < 2:
                continue
            monkey_info[monkey][info_split[0]] = info_split[1].strip(" ")

    modulus = [int(monkey_info[monkey]["Test"].split(" ")[-1]) for monkey in monkey_info]
    lcm = math.lcm(*modulus)

def perform_operation(monkey):
    worry_level = monkey_info[monkey]["Starting items"]
    operation_info = monkey_info[monkey]["Operation"].split(" ")
    determ_val = operation_info[-1]
    for i in range(len(worry_level)):
        actual_val = worry_level[i] if determ_val == "old" else determ_val
        worry_level[i] = eval(str(worry_level[i]) + str(operation_info[-2]) + str(actual_val))
        # Part 1.
        # worry_level[i] //= 3

        # Part 2.
        worry_level[i] = int(worry_level[i]) % lcm
        monkey_info[monkey]["Num inspections"] += 1

    monkey_info[monkey]["Starting items"] = worry_level


def test(monkey):
    worry_level = monkey_info[monkey]["Starting items"]
    monkey_info[monkey]["Starting items"] = []
    for level in worry_level:
        test_result = "If " + str(int(level) % int(monkey_info[monkey]["Test"].split(" ")[-1]) == 0).lower()
        throw_to = "monkey " + monkey_info[monkey][test_result].split(" ")[-1] + ":"
        # Part 1.
        monkey_info[throw_to]["Starting items"].append(level)



if __name__ == "__main__":
    num_rounds = 10000
    for _ in tqdm(range(num_rounds)):
        for monkey in monkey_info:
            perform_operation(monkey)
            test(monkey)

    count_inspections = sorted([monkey_info[monkey]["Num inspections"] for monkey in monkey_info], reverse=True)
    print("Amount of monkey business is " + str(count_inspections[0] * count_inspections[1]))