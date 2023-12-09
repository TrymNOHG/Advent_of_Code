register = 1


def add_pixel(pos, pixel):
    return "#" if (pixel - 1) % 40 in [pos - 1, pos, pos + 1] else "."


with open("input.txt") as message:
    strengths = []
    screen = []
    current_row = ""
    cycle = 1
    current_row += add_pixel(register, cycle)
    for instruct in message.readlines():
        if "noop" in instruct:
            cycle += 1
        else:
            command, value = instruct.strip("\n").split(" ")
            cycle += 1

            current_row += add_pixel(register, cycle)
            if cycle % 40 == 20:
                strengths.append(register * cycle)

            if cycle % 40 == 0:
                screen.append(current_row)
                current_row = ""

            register += int(value)
            cycle += 1

        current_row += add_pixel(register, cycle)

        if cycle % 40 == 20:
            strengths.append(register * cycle)

        if cycle % 40 == 0:
            screen.append(current_row)
            current_row = ""

if __name__ == "__main__":
    print("Sum of strengths: " + str(sum([strengths[i] for i in range(6)])))
    for row in screen:
        print(row)
