class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.value} : {self.left}, {self.right}"


def part1(file):
    instructions = file.readline().strip("\n")
    file.readline()
    nodes = {}
    for index, line in enumerate(file):
        splits = line.strip("\n").replace("(", "").replace(")", "").replace(",", "").split(" ")
        if nodes.get(splits[0]) is None:
            nodes[splits[0]] = Node(splits[0], splits[2], splits[3])
        else:
            node = nodes[splits[0]]
            node.left = splits[2]
            node.right = splits[3]

    node_val = 'AAA'
    instruct_index = 0
    number_of_instructions = len(instructions)
    while node_val != 'ZZZ':
        if instructions[instruct_index % number_of_instructions] == 'L':
            node_val = nodes[node_val].left
        else:
            node_val = nodes[node_val].right
        instruct_index += 1

    print(instruct_index)

    for node in nodes.values():
        print(node)


def part2(file):
    instructions = file.readline().strip("\n")
    file.readline()
    nodes = {}
    for index, line in enumerate(file):
        splits = line.strip("\n").replace("(", "").replace(")", "").replace(",", "").split(" ")
        if nodes.get(splits[0]) is None:
            nodes[splits[0]] = Node(splits[0], splits[2], splits[3])
        else:
            node = nodes[splits[0]]
            node.left = splits[2]
            node.right = splits[3]

    node_start_val = 'A'
    start_nodes = []
    for node in nodes.values():
        if node.value[-1] == node_start_val:
            start_nodes.append(node)

    # for node in start_nodes:
    #     print(node)
    instruct_index = 0
    number_of_instructions = len(instructions)

    all_reached_end = False
    while not all_reached_end:
        # Check if all reached
        all_reached_end = True
        if instructions[instruct_index % number_of_instructions] == 'L':
            for index, node in enumerate(start_nodes):
                start_nodes[index] = nodes[node.left]
        else:
            for index, node in enumerate(start_nodes):
                start_nodes[index] = nodes[node.right]

        for index, node in enumerate(start_nodes):
            for other_index, other_node in enumerate(start_nodes):
                if index != other_index:
                    if node.value == other_node.value:
                        start_nodes.pop(other_index)

        instruct_index += 1
        for index, node in enumerate(start_nodes):
            if node.value[-1] != 'Z':
                all_reached_end = False
                break

    print(instruct_index)

    # for node in nodes.values():
    #     print(node)


with open("input.txt", "r") as file:
    # part1(file)
    part2(file)
