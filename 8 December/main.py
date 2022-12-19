# In order to optimize this, look into creating a linked list/graph of nodes connected to neighbors.
# Right now, a neighbor table is created using a 2D array. Searching for neighbors is therefore not super effective.
global visible_trees


class Tree:
    def __init__(self, height=0, visible=False):
        self.height = height
        self.visible = visible

    def __repr__(self):
        return "(" + str(self.height) + ", " + str(self.visible) + ")"


forest_grid = [[Tree(int(number)) for number in line.strip("\n")] for line in open("input.txt").readlines()]

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
            print(forest_grid[row][column])
            is_Tree_Visible(row, column)


def row_valid(row):
    return 0 <= row < len(forest_grid)


def column_valid(column):
    return 0 <= column < len(forest_grid[0])


def valid_index(row, column):
    return row_valid(row) and column_valid(column)


def tree_taller(treeA, treeB):
    return treeA.height > treeB.height


def check_vertical_treeline(row, column):
    current_tree = forest_grid[row][column]
    max_height = 0
    for i in range(row):
        if forest_grid[i][column].height > forest_grid[max_height][column].height:
            max_height = i

    if tree_taller(current_tree, forest_grid[max_height][column]):
        current_tree.visible = True
        return

    max_height = row + 1

    for i in range(row + 1, len(forest_grid)):
        if forest_grid[i][column].height > forest_grid[max_height][column].height:
            max_height = i

    if tree_taller(current_tree, forest_grid[max_height][column]):
        current_tree.visible = True
        return

    return


def check_horizontal_treeline(row, column):
    current_tree = forest_grid[row][column]
    max_height = 0
    for i in range(column):
        if forest_grid[row][i].height > forest_grid[row][max_height].height:
            max_height = i

    if tree_taller(current_tree, forest_grid[row][max_height]):
        current_tree.visible = True
        return

    max_height = column + 1
    for i in range(column + 1, len(forest_grid[0])):
        if forest_grid[row][i].height > forest_grid[row][max_height].height:
            max_height = i

    if tree_taller(current_tree, forest_grid[row][max_height]):
        current_tree.visible = True
        return

    return


def is_Tree_Visible(row, column):
    global visible_trees

    check_vertical_treeline(row, column)
    check_horizontal_treeline(row, column)

    if forest_grid[row][column].visible:
        visible_trees += 1

    return


def is_Tree_Visible_diagonally(row, column):
    current_tree = forest_grid[row][column]
    global visible_trees
    if current_tree.visible is True:
        return
    for neighbor_row in range(-1, 2):
        for neighbor_column in range(-1, 2):
            if valid_index(row + neighbor_row, column + neighbor_column):
                neighbor_tree = forest_grid[row + neighbor_row][column + neighbor_column]
                if tree_taller(current_tree, neighbor_tree) and neighbor_tree.visible is True:
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
    for row in forest_grid:
        print(row)
    find_visible_trees()
    print("The total number of visible trees is : " + str(visible_trees))
    for row in forest_grid:
        print(row)
