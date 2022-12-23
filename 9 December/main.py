# It could be smart to use a set in order to hold all the visited nodes. I could also have a visited boolean.
# I could use linked lists in order to represent the network of nodes.
class Node:
    """
        This node represents the different locations on the network grid.
    """

    def __init__(self, x_coord=0.0, y_coord=0.0):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def update_coord(self, move_dir):
        directions = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
        move_tup = directions.get(move_dir)
        self.x_coord += move_tup[0]
        self.y_coord += move_tup[1]

    def fully_update_coord(self, move):
        for _ in range(int(move[1])):
            self.update_coord(move[0])

    def __repr__(self):
        return str(self.x_coord) + ", " + str(self.y_coord)


head_node = Node()
head_prev_loc = Node()
tail_node = Node()

instructions = [(move.strip("\n").split(" ")[0], move.strip("\n").split(" ")[1])
                for move in open("input.txt").readlines()]


def need_move(head, tail, prev_loc):
    """
    Using some simple algebra, this method checks if the head node is within a distance of sqrt(2)
    from the tail node.
    If so, then the tail node will not move. If not, the tail node needs to move to the head node's previous position.
    """

    dist = ((head.x_coord - tail.x_coord) ** 2
            + (head.y_coord - tail.y_coord) ** 2) ** 0.5
    if not (-(2 ** 0.5) <= dist <= (2 ** 0.5)):
        tail.x_coord, tail.y_coord = prev_loc.x_coord, prev_loc.y_coord


def sign(num):
    return -1 if num < 0 else 1


def make_move(head, tail):
    moves = {(tail.x_coord, tail.y_coord)}
    x_diff = head.x_coord - tail.x_coord
    y_diff = head.y_coord - tail.y_coord

    while not (-(2 ** 0.5) <= (x_diff ** 2 + y_diff ** 2) ** 0.5 <= (2 ** 0.5)):
        if x_diff != 0:
            tail.x_coord += sign(x_diff)
            x_diff = head.x_coord - tail.x_coord
        if y_diff != 0:
            tail.y_coord += sign(y_diff)
            y_diff = head.y_coord - tail.y_coord
        moves.add((tail.x_coord, tail.y_coord))

    return moves


Part 1
tail_moves = {(0, 0)}  # A set of the coordinate positions of the tail node.
for move in instructions:
    for i in range(int(move[1])):
        head_prev_loc.x_coord, head_prev_loc.y_coord = head_node.x_coord, head_node.y_coord
        head_node.update_coord(move[0])
        need_move(head_node, tail_node, head_prev_loc)
        tail_moves.add((tail_node.x_coord, tail_node.y_coord))
        # print("Head " + str(head_node))
        # print("Tail " + str(tail_node))

print(len(tail_moves))

# Part 2
nodes = [Node() for i in range(10)]
tail_moves = {(0, 0)}  # A set of the coordinate positions of the tail node.
for move in instructions:
    nodes[0].fully_update_coord(move)  # Head node
    print("Head " + str(nodes[0]))
    for j in range(len(nodes) - 1):
        moves_made = make_move(nodes[j], nodes[j + 1])
        print("Tail " + str(j + 1) + ". " + str(nodes[j + 1]))
        if j == len(nodes) - 2:
            tail_moves |= moves_made

print(sorted(tail_moves))
print(len(tail_moves))

if __name__ == '__main__':
    print()
