# In order to optimize this, look into creating a linked list/graph of nodes connected to neighbors.
# Right now, a neighbor table is created using a 2D array. Searching for neighbors is therefore not super effective.
global visible_trees


class Tree:
    def __init__(self, height=0, visible=False):
        self.height = height
        self.visible = visible

    def __repr__(self):
        return "(" + str(self.height) + ", " + str(self.visible) + ")"


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
            print(forest_grid[row][column])
            is_Tree_Visible(row, column)


def row_valid(row):
    return 0 <= row < len(forest_grid)


def column_valid(column):
    return 0 <= column < len(forest_grid[0])


def tree_taller(treeA, treeB):
    return treeA.height > treeB.height


def is_Tree_Visible(row, column):
    global visible_trees
    if forest_grid[row][column].visible is True:
        return
    for i in range(3):
        for neighbor_row in range(3):
            for neighbor_column in range(3):
                if row_valid(row + neighbor_row - 1) and column_valid(column + neighbor_column - 1):
                    if tree_taller(forest_grid[row - 2 - neighbor_row][column + neighbor_column - 1],
                                   forest_grid[row][column]) and \
                            forest_grid[row - 2 - neighbor_row][column + neighbor_column - 1].visible is True:
                        forest_grid[row][column].visible = True
                        visible_trees += 1
                        if row_valid(row + (neighbor_row - 1) * - 1) and \
                                column_valid(column + (neighbor_column - 1) * - 1):
                            is_Tree_Visible(row + (neighbor_row - 1) * - 1, column + (neighbor_column - 1) * - 1)
                        continue
    return


if __name__ == "__main__":
    find_visible_trees()
    print("The total number of visible trees is : " + str(visible_trees))
    for row in forest_grid:
        print(row)
