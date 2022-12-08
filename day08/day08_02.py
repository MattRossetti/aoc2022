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


# making assumption that outer layer will not have best scenic score
tree_scores = []
for tree in inner_trees:
    y = tree[0]
    x = tree[1]
    # check up
    up_count = 0
    y2 = y
    while y2 > 0:
        if grid[y][x] <= grid[y2 - 1][x]:
            up_count += 1
            break
        up_count += 1
        y2 -= 1
    # check right
    right_count = 0
    x2 = x
    while x2 < grid_length - 1:
        if grid[y][x] <= grid[y][x2 + 1]:
            right_count += 1
            break
        right_count += 1
        x2 += 1
    # check left
    left_count = 0
    x2 = x
    while x2 > 0:
        if grid[y][x] <= grid[y][x2 - 1]:
            left_count += 1
            break
        left_count += 1
        x2 -= 1
    # check down
    down_count = 0
    y2 = y
    while y2 < grid_height - 1:
        if grid[y][x] <= grid[y2 + 1][x]:
            down_count += 1
            break
        down_count += 1
        y2 += 1
    scenic_score = up_count * right_count * left_count * down_count
    tree_scores.append(scenic_score)

answer = max(tree_scores)
print(f"answer: {answer}")
