alphabet = {chr(ord('a') + i): i + 1 for i in range(26)}  # Add the first letters of the alphabet

for i in range(26):
    alphabet[chr(ord('A') + i)] = 26 + i + 1


def find_wrong_item():
    items = [letter for letter in line]
    compartment_size = len(items) >> 1
    first_compartment = [items[i] for i in range(compartment_size)]
    second_compartment = [items[i] for i in range(compartment_size, len(items))]

    first_compartment_map = {}
    second_compartment_map = {}

    for i in range(compartment_size):

        first_compartment_map[first_compartment[i]] = 1
        second_compartment_map[second_compartment[i]] = 1
        if first_compartment_map.get(second_compartment[i]) is not None:
            return alphabet.get(second_compartment[i])
        if second_compartment_map.get(first_compartment[i]) is not None:
            return alphabet.get(first_compartment[i])

    return None


def fill_map(list_of_letters):
    compartment_map = {}
    for letter in list_of_letters:
        compartment_map[letter] = 1

    return compartment_map


def find_badges():
    first_compartment = [letter for letter in group[0]]
    second_compartment = [letter for letter in group[1]]
    third_compartment = [letter for letter in group[2]]

    first_compartment_map = fill_map(first_compartment)
    second_compartment_map = fill_map(second_compartment)

    for letter in third_compartment:
        if first_compartment_map.get(letter) is not None and second_compartment_map.get(letter) is not None:
            return alphabet.get(letter)
    return None


with open("input.txt") as compartments:
    total_prio = 0
    total_prio_badge = 0
    i = 0
    group = ["", "", ""]
    for line in compartments:
        print("Priority of wrong item: " + str(find_wrong_item()))
        total_prio += find_wrong_item()
        group[i] = line
        if i == 2:
            total_prio_badge += find_badges()
            group = ["", "", ""]
            i = -1
        i += 1

    print("The total priority: " + str(total_prio))
    print("The total badge priority: " + str(total_prio_badge))

if __name__ == '__main__':
    print()
