# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def get_max_calories():
    list_of_calories = []
    total_calories = 0
    max_cal = 0
    for line in elf_calories:
        if line == "\n":
            list_of_calories.append(total_calories)
            if total_calories > max_cal:
                max_cal = total_calories
            total_calories = 0
        else:
            total_calories += int(line)

    print("Maximum calories carried by an elf is " + str(max_cal))
    return list_of_calories


def get_top_three(calorie_list):
    calorie_list.sort(reverse=True)
    total = 0
    for i in range(3):
        total += calorie_list[i]
        print(calorie_list[i])

    print("The three elves carrying the most are carrying " + str(total) + " calories")


with open("calories.txt") as elf_calories:
    list_of_calories = get_max_calories()
    get_top_three(list_of_calories)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print()
