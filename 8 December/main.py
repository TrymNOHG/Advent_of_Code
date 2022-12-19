# In order to optimize this, look into creating a linked list/graph of nodes connected to neighbors.
# Right now, a neighbor table is created using a 2D array. Searching for neighbors is therefore not super effective.
global visible_trees


class Tree:
    def __init__(self, height=0, visible=False, scenic_score=0):
        self.height = height
        self.visible = visible
        self.scenic_score = scenic_score

    def __repr__(self):
        return "(" + str(self.height) + ", " + str(self.visible) + ", " + str(self.scenic_score) + ")"


forest_grid = [[Tree(int(number)) for number in line.strip("\n")] for line in open("test.txt").readlines()]

for column in range(len(forest_grid[0])):
    forest_grid[0][column].visible = True
    forest_grid[len(forest_grid) - 1][column].visible = True

for row in range(len(forest_grid)):
    forest_grid[row][0].visible = True
    forest_grid[row][len(forest_grid[0]) - 1].visible = True

visible_trees = int((len(forest_grid) + len(forest_grid[0]) - 2) << 1)


def find_visible_trees():
    for row in range(1, len(forest_grid[0]) - 1):
        for column in range(1, len(forest_grid[0]) - 1):
            is_Tree_Visible(row, column)


def row_valid(row):
    return 0 <= row < len(forest_grid)


def column_valid(column):
    return 0 <= column < len(forest_grid[0])


def valid_index(row, column):
    return row_valid(row) and column_valid(column)


def tree_taller(treeA, treeB):
    return treeA.height >= treeB.height


def check_vertical_treeline(row, column):
    current_tree = forest_grid[row][column]
    top_view_score = 0
    print(current_tree)
    for i in range(1, row + 1):
        print(forest_grid[row - i][column])
        if tree_taller(forest_grid[row - i][column], current_tree):
            top_view_score = i
            break

    if top_view_score == 0:
        current_tree.visible = True
        top_view_score = row
    print(current_tree)

    bottom_view_score = 0
    for i in range(1, len(forest_grid) - row):
        if tree_taller(forest_grid[row + i][column], current_tree):
            bottom_view_score = i
            break

    if bottom_view_score == 0:
        current_tree.visible = True
        bottom_view_score = len(forest_grid) - row - 1

    return top_view_score, bottom_view_score


def check_horizontal_treeline(row, column):
    current_tree = forest_grid[row][column]
    left_view_score = 0
    for i in range(1, column + 1):
        if tree_taller(forest_grid[row][column - i], current_tree):
            left_view_score = i
            break

    if left_view_score == 0:
        current_tree.visible = True
        left_view_score = column

    right_view_score = 0
    for i in range(1, len(forest_grid[0]) - column):
        if tree_taller(forest_grid[row][column + i], current_tree):
            right_view_score = i
            break

    if right_view_score == 0:
        current_tree.visible = True
        right_view_score = len(forest_grid[0]) - column - 1

    return left_view_score, right_view_score


def is_Tree_Visible(row, column):
    global visible_trees

    top_score, bottom_score = check_vertical_treeline(row, column)
    left_score, right_score = check_horizontal_treeline(row, column)

    forest_grid[row][column].scenic_score = top_score * bottom_score * left_score * right_score

    if forest_grid[row][column].visible:
        visible_trees += 1

    return


def find_max_scenic_score():
    max_score = 0
    for row in forest_grid:
        for tree in row:
            if tree.scenic_score > max_score:
                max_score = tree.scenic_score

    return max_score


def is_Tree_Visible_diagonally(row, column):
    current_tree = forest_grid[row][column]
    global visible_trees
    if current_tree.visible is True:
        return
    for neighbor_row in range(-1, 2):
        for neighbor_column in range(-1, 2):
            if valid_index(row + neighbor_row, column + neighbor_column):
                neighbor_tree = forest_grid[row + neighbor_row][column + neighbor_column]
                if current_tree.height > neighbor_tree.height and neighbor_tree.visible is True:
                    current_tree.visible = True
                    visible_trees += 1
                    if valid_index(row + neighbor_row * - 1, column + neighbor_column * - 1):
                        is_Tree_Visible_diagonally(row + neighbor_row * - 1, column + neighbor_column * - 1)
                    continue
    return


"""
    This solution includes looking diagonally, which is an extension of the original problem.
"""

if __name__ == "__main__":
    find_visible_trees()
    print("The total number of visible trees is : " + str(visible_trees))
    print("The max scenic score is: " + str(find_max_scenic_score()))
    for tree in forest_grid:
        print(tree)
