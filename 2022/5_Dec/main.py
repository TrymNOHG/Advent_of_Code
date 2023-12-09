# This assignment seems to imitate the tower of hanoi problem.
# However, instead of poles and rings we have crates and stacks.
class Crate:
    def __init__(self, character):
        self.character = character


class Stack:
    def __init__(self, crates):
        self.crates = crates

    def add(self, crate):
        self.crates.append(crate)

    def add_first(self, crate):
        self.crates.insert(0, crate)

    def pop(self):
        return self.crates.pop(0)

    def remove(self, crate):
        self.crates.remove(crate)


list_of_stacks = []
for i in range(9):
    list_of_stacks.append(Stack([]))


def add_to_stacks():
    current_stack = 0
    for ch in line.strip("\n").replace("[", "").replace("]", "").split(" "):
        if ch != "":
            list_of_stacks[int(current_stack)].add(Crate(ch))
            current_stack += 1
        else:
            current_stack += 0.25


def perform_move():
    moves = line.strip("\n").replace("move ", "").replace(" from", "").replace(" to", "").split(" ")
    amount_to_move = int(moves[0])
    from_stack = list_of_stacks[int(moves[1]) - 1]
    to_stack = list_of_stacks[int(moves[2]) - 1]

    for move in range(amount_to_move):
        to_stack.add_first(from_stack.pop())
    # Perform the actual moves here...


def perform_mult_move():
    moves = line.strip("\n").replace("move ", "").replace(" from", "").replace(" to", "").split(" ")
    amount_to_move = int(moves[0])
    from_stack = list_of_stacks[int(moves[1]) - 1]
    temp_stack = Stack([])
    to_stack = list_of_stacks[int(moves[2]) - 1]

    for move in range(amount_to_move):
        temp_stack.add_first(from_stack.pop())

    for move in range(amount_to_move):
        to_stack.add_first(temp_stack.pop())

    # Perform the actual moves here...


with open("input.txt") as crate_info:
    crate_start_info = True
    for line in crate_info:  # This for loop handles the loading of the crates onto the stacks
        if line.strip(" ").split(" ")[0] == "1":
            crate_start_info = False
            crate_info.readline()
            break
        if crate_info:
            add_to_stacks()

    # Check that the stacks are correct
    for line in crate_info:  # This for loop handles the actual moving of crates
        # perform_move() first assignment
        perform_mult_move()

    top_crate_ch = ""
    for stack in list_of_stacks:
        if len(stack.crates) != 0:
            top_crate_ch += str(stack.pop().character)

    print(top_crate_ch)

if __name__ == '__main__':
    print()
