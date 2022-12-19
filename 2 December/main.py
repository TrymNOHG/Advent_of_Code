class ActionNode:
    """
        This is a node class, representing the different actions you can do in rock paper scissors.
    """

    def __init__(self, action, additional_points, edge=None):
        self.action = action
        self.additional_points = additional_points
        self.edge = edge


class MoveEdge:
    """
        This class represents the different moves that can occur between action nodes.
        It can be thought of as a weighted edge in a graph.
    """

    def __init__(self, score, to_node, next=None):
        self.score = score
        self.next = next
        self.to_node = to_node


def create_game_graph():
    rock_action = ActionNode("Rock", 1)
    paper_action = ActionNode("Paper", 2)
    scissors_action = ActionNode("Scissors", 3)

    rock_action.edge = MoveEdge(6, scissors_action)
    rock_action.edge.next = MoveEdge(0, paper_action)
    rock_action.edge.next.next = MoveEdge(3, rock_action)

    paper_action.edge = MoveEdge(0, scissors_action)
    paper_action.edge.next = MoveEdge(3, paper_action)
    paper_action.edge.next.next = MoveEdge(6, rock_action)

    scissors_action.edge = MoveEdge(3, scissors_action)
    scissors_action.edge.next = MoveEdge(6, paper_action)
    scissors_action.edge.next.next = MoveEdge(0, rock_action)

    return {"Rock": rock_action, "Paper": paper_action, "Scissors": scissors_action}


graph = create_game_graph()


def create_map():
    return {"A": "Rock", "B": "Paper", "C": "Scissors",
            "X": "Rock", "Y": "Paper", "Z": "Scissors"}


moves = create_map()


def determine_winner():
    """
        This method plays out a regular game of rock paper scissors and returns the value of whether you won or not.
    """
    opponent_move, my_move = line.strip("\n").split(" ")
    opponent_move = moves.get(opponent_move)
    my_move = moves.get(my_move)

    action_node = graph.get(my_move)

    action_edge = action_node.edge
    while action_edge is not None:
        if action_edge.to_node.action == opponent_move:
            return action_edge.score + action_node.additional_points
        else:
            action_edge = action_edge.next


rigged_map = {"X": 6, "Y": 3, "Z": 0}


def determine_score():
    """
        Part 2 of calendar.
    """
    opponent_move, my_move = line.strip("\n").split(" ")
    opponent_move = moves.get(opponent_move)
    result_score = rigged_map.get(my_move)

    action_node = graph.get(opponent_move)

    action_edge = action_node.edge
    while action_edge is not None:
        if action_edge.score == result_score:
            return action_edge.to_node.additional_points + (6 - result_score)
        else:
            action_edge = action_edge.next


with open("input.txt") as move_list:
    my_total_score = 0
    my_rigged_score = 0
    for line in move_list:
        my_total_score += determine_winner()
        my_rigged_score += determine_score()
        print(determine_score())

    print("My total score was: " + str(my_total_score))

    print("In the rigged game, my score was " + str(my_rigged_score))

if __name__ == '__main__':
    print()
