with open("input.txt") as file:
    lines = file.read().splitlines()
    grid = []
    for line in lines:
        row = []
        for char in line:
            row.append(char)
        grid.append(row)


def is_edge(x, y, grid_length, grid_height):
    if x == 0 or x == grid_length - 1:
        return True
    if y == 0 or y == grid_height - 1:
        return True
    return False


def is_inner(x, y, grid_length, grid_height):
    if x != 0 and x != grid_length - 1 and y != 0 and y != grid_height - 1:
        return True


edge_trees = []
inner_trees = []
grid_height = len(grid)
grid_length = len(grid[0])
for i in range(grid_height):
    for j in range(grid_length):
        if is_edge(j, i, grid_length, grid_height):
            edge_trees.append((i, j))
        if is_inner(j, i, grid_length, grid_height):
            inner_trees.append((i, j))


visible_trees = []
for tree in inner_trees:
    y = tree[0]
    x = tree[1]
    # check up
    visible_up = True
    y2 = y
    while y2 > 0:
        if grid[y][x] <= grid[y2 - 1][x]:
            visible_up = False
            break
        y2 -= 1
    # check right
    visible_right = True
    x2 = x
    while x2 < grid_length - 1:
        if grid[y][x] <= grid[y][x2 + 1]:
            visible_right = False
            break
        x2 += 1
    # check left
    visible_left = True
    x2 = x
    while x2 > 0:
        if grid[y][x] <= grid[y][x2 - 1]:
            visible_left = False
            break
        x2 -= 1
    # check down
    visible_down = True
    y2 = y
    while y2 < grid_height - 1:
        if grid[y][x] <= grid[y2 + 1][x]:
            visible_down = False
            break
        y2 += 1
    if visible_up or visible_right or visible_left or visible_down:
        visible_trees.append(tree)

answer = len(edge_trees) + len(visible_trees)
print(f"answer: {answer}")
