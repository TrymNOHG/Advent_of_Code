# Split each line by comma to get interval of one elf, split interval by - to get the min and max bounds

def is_subset():
    id_pairs = id_pair.split(",")

    first_id_interval = id_pairs[0].split("-")
    second_id_interval = id_pairs[1].split("-")

    first_comparison = -1
    second_comparison = -1
    if int(first_id_interval[0]) < int(second_id_interval[0]):
        first_comparison = 1

    elif int(first_id_interval[0]) == int(second_id_interval[0]):
        first_comparison = 0

    if int(first_id_interval[1]) > int(second_id_interval[1]):
        second_comparison = 1

    elif int(first_id_interval[1]) == int(second_id_interval[1]):
        second_comparison = 0

    if first_comparison * second_comparison == -1:
        return 0

    return 1


"""
    This method is basically a comparator of the different intervals. 
"""


def is_overlap():
    id_pairs = id_pair.split(",")

    first_lower, first_upper = id_pairs[0].split("-")
    second_lower, second_upper = id_pairs[1].split("-")
    if (int(first_upper) - int(second_lower)) * (int(first_lower) - int(second_lower)) <= 0:
        return 1
    elif (int(first_upper) - int(second_upper)) * (int(first_lower) - int(second_upper)) <= 0:
        return 1
    else:
        return is_subset()


with open("input.txt") as ids:
    total_subset_pairs = 0
    total_overlap = 0
    for id_pair in ids:
        total_subset_pairs += is_subset()
        total_overlap += is_overlap()

    print("In how many assignment pairs does one range fully contain the other?")
    print(total_subset_pairs)
    print("In how many assignment pairs do the ranges overlap?")
    print(total_overlap)

if __name__ == '__main__':
    print()
