# In this challenge, Dijkstra's algorithm can be used.
# The edges are all the places where one letter is up, down, left, or right from another letter.

class Previous:
    def __init__(self, prev_node=None, distance=100000000):
        self.prev_node = prev_node
        self.distance = distance
class Node:
    def __init__(self, index, element, previous=Previous(), edge=None):
        self.index = index
        self.element = element
        self.previous = previous
        self.edge = edge

    def __lt__(self, other_node):
        return self.previous.distance < other_node.previous.distance
    def __gt__(self, other_node):
        return self.previous.distance > other_node.previous.distance

    def __eq__(self, other):
        return self.element == other

    def __repr__(self):
        return str(self.index) + ". " + str(self.previous.distance)

    def add_edge(self, edge):
        if self.edge is None:
            self.edge = edge
        else:
            self.edge.add_edge(edge)
class Edge:
    def __init__(self, to_node : Node, symbol,  next_edge=None):
        self.to_node = to_node
        self.symbol = symbol
        self.next_edge = next_edge

    def __repr__(self):
        return str(self.symbol) + " " + str(self.to_node)

    def add_edge(self, edge):
        if self.next_edge is None:
            self.next_edge = edge
        else:
            self.next_edge.add_edge(edge)


def parent(index:int)-> int:
    return (index - 1) >> 1


def left_child(index:int)-> int:
    return (index << 1) + 1


def right_child(index:int)-> int:
    return (index + 1) << 1


def has_parent(index:int):
    return parent(index) >= 0


class MinHeap:
    def __init__(self, nodes=None):
        if nodes is None:
            nodes = []
        self.nodes = nodes
        self.fix_heap()


    def add(self, node:Node):
        self.nodes.append(node)
        self.heapify_up(len(self.nodes) - 1)

    def fix_heap(self):
        num_iterations = len(self.nodes)//2 - 1
        for i in range(num_iterations, -1, -1):
            self.heapify_down(i)


    def heapify_up(self, index:int):
        current_node = self.nodes[index]
        if has_parent(index):
            parent_index = parent(index)
            if self.nodes[parent_index] > current_node:
                self.swap(index, parent_index)
                self.heapify_up(parent_index)

    def heapify_down(self, index: int):
        current_node = self.nodes[index]
        if self.has_left(index):
            left_index = left_child(index)
            if self.has_right(index) and self.nodes[left_index] > self.nodes[left_index + 1]:
                left_index += 1
            if current_node > self.nodes[left_index]:
                self.swap(index, left_index)
                self.heapify_down(left_index)

    def peek(self):
        return self.nodes[0] if len(self.nodes) > 0 else None


    def poll(self)-> Node or None:
        self.swap(0, len(self.nodes) - 1)
        root = self.nodes.pop()
        if len(self.nodes) > 0:
            self.heapify_down(0)
        return root

    def has_left(self, index:int):
        return left_child(index) < len(self.nodes)

    def has_right(self, index:int):
        return right_child(index) < len(self.nodes)

    def swap(self, index1:int, index2:int):
        temp = self.nodes[index1]
        self.nodes[index1] = self.nodes[index2]
        self.nodes[index2] = temp


start = 'S'
end = 'E'

with open("input.txt", mode="r") as path:
# Create nodes and edges
#First 2d array in order to easily create edges. Then convert to single array
    index = 0
    input_2d = []
    for line in path:
        input_2d.append([])
        for letter in line.strip():
            input_2d[-1].append(Node(index, letter, Previous()))
            index += 1

    # -> and <- edges
    for row in range(len(input_2d)):
        for column in range(len(input_2d[row]) - 1):
            current_letter = 'a' if input_2d[row][column] == start else 'z' if input_2d[row][column] == end else \
            input_2d[row][column].element
            next_letter = 'a' if input_2d[row][column + 1] == start else 'z' if input_2d[row][column + 1] == end else \
            input_2d[row][column + 1].element
            if abs(ord(current_letter) - ord(next_letter)) <= 1:
                input_2d[row][column].add_edge(Edge(input_2d[row][column + 1], "->"))
                input_2d[row][column + 1].add_edge(Edge(input_2d[row][column], "<-"))


    # ^ and v edges
    for column in range(len(input_2d[0])):
        for row in range(len(input_2d) - 1, 0, -1):
            current_letter = 'a' if input_2d[row][column] == start else 'z' if input_2d[row][column] == end \
                else input_2d[row][column].element
            next_letter = 'a' if input_2d[row - 1][column] == start else 'z' if input_2d[row - 1][column] == end \
                else input_2d[row - 1][column].element
            if abs(ord(current_letter) - ord(next_letter)) <= 1:
                input_2d[row][column].add_edge(Edge(input_2d[row - 1][column], "^"))
                input_2d[row - 1][column].add_edge(Edge(input_2d[row][column], "v"))

    node_list = [node for row in input_2d for node in row]


def init_prev():
    for node in node_list:
        if node.element == start:
            node.previous.distance = 0
            break

def optimize_dist(previous_node, node):
    if node.index == 2485:
        print(previous_node)
        print("ok")
    if previous_node.previous.distance + 1 < node.previous.distance:
        node.previous.distance = previous_node.previous.distance + 1
        node.previous.prev_node = previous_node
        if node.index == 2326:
            print("ok")

def dijkstra_algorithm():
    init_prev()
    min_heap = MinHeap(node_list)
    current_node = None
    while len(min_heap.nodes) > 0:
        current_node = min_heap.poll()
        if current_node.element == end:
            return current_node
        node_edge = current_node.edge
        while node_edge is not None:
            optimize_dist(current_node, node_edge.to_node)
            node_edge = node_edge.next_edge
        min_heap.fix_heap()

    return current_node


if __name__ == "__main__":
    final_node = dijkstra_algorithm()
    print("Final distance is: " + str(final_node.previous.distance))
    # previous_node = final_node
    # while previous_node is not None:
    #     length += 1
    #     previous_node = previous_node.previous.prev_node

