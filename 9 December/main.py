# It could be smart to use a set in order to hold all the visited nodes. I could also have a visited boolean.
# I could use linked lists in order to represent the network of nodes.

class Node:
    """
        This node represents the different locations on the network grid.
    """
    def __init__(self, edges=None, head=False):
        self.edges = edges
        self.head = head





class Edge:
    """
        This edge represents the different paths the tail can take from a given node.
    """
    def __init__(self, other_edge, to_node):
        self.other_edge = other_edge
        self.to_node = to_node





class Network:
    def __init__(self, nodes=None):
        self.nodes = nodes

    def add_column(self):
        for row in self.nodes:
            row.append(Node())

    def add_row(self):
        nodes_needed = len(self.nodes[0])
        self.nodes.append([])
        for i in range(nodes_needed):
            self.nodes[-1].append(Node())


if __name__ == '__main__':
    list_of_things = [1, 2, 5]
    print(list_of_things[-1])
