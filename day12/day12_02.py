from queue import PriorityQueue


with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    grid = []
    row_id = 0
    for line in lines:
        row = []
        for i, char in enumerate(line):
            if char == "S":
                start_loc = (row_id, i)
                char = "a"
            if char == "E":
                end_loc = (row_id, i)
                char = "z"
            row.append(char)
        row_id += 1
        grid.append(row)


def is_location_inbounds(location, grid, grid_rows, grid_columns):
    if location[0] < 0 or location[1] < 0:
        return False
    if location[0] >= grid_rows or location[1] >= grid_columns:
        return False
    try:
        grid[location[0]][location[1]]
    except IndexError:
        return False
    return True


def is_move_valid(height, neighbor_height):
    if ord(neighbor_height) - ord(height) > 1:
        return False
    return True


pq = PriorityQueue()
pq.put((0, (start_loc)))
visited = set()
grid_rows = len(grid)
grid_columns = len(grid[0])

found = False
count = 0
while found is False:
    count += 1
    steps, (loc) = pq.get()
    # print(pq.qsize())
    # print(loc)
    height = grid[loc[0]][loc[1]]
    # if at end, set found to True and continue
    if (loc) == end_loc:
        answer = steps
        print("answer: ", answer)
        found = True
        continue
    # if been at spot before, continue, else add loc to visited
    if (loc) in visited:
        # print("been here before")
        continue
    visited.add(loc)
    # if up is valid and inbounds, add up to pq with steps incremented
    up_loc = (loc[0] - 1, loc[1])
    up_location_inbounds = is_location_inbounds(
        (up_loc), grid, grid_rows, grid_columns)
    if up_location_inbounds:
        up_move_valid = is_move_valid(height, grid[up_loc[0]][up_loc[1]])
        if up_move_valid:
            # print("up")
            if height == "a":
                steps = 0
            pq.put((steps + 1, (up_loc)))
    # if right is valid and inbounds, add right to pq with steps incremented
    right_loc = (loc[0], loc[1] + 1)
    right_location_inbounds = is_location_inbounds(
        (right_loc), grid, grid_rows, grid_columns)
    if right_location_inbounds:
        right_move_valid = is_move_valid(
            height, grid[right_loc[0]][right_loc[1]])
        if right_move_valid:
            # print("right")
            if height == "a":
                steps = 0
            pq.put((steps + 1, (right_loc)))
    # if down is valid and inbounds, add down to pq with steps incremented
    down_loc = (loc[0] + 1, loc[1])
    down_location_inbounds = is_location_inbounds(
        (down_loc), grid, grid_rows, grid_columns)
    if down_location_inbounds:
        down_move_valid = is_move_valid(height, grid[down_loc[0]][down_loc[1]])
        if down_move_valid:
            # print("down")
            if height == "a":
                steps = 0
            pq.put((steps + 1, (down_loc)))
    # if left is valid and inbounds, add left to pq with steps incremented
    left_loc = (loc[0], loc[1] - 1)
    left_location_inbounds = is_location_inbounds(
        (left_loc), grid, grid_rows, grid_columns)
    if left_location_inbounds:
        left_move_valid = is_move_valid(height, grid[left_loc[0]][left_loc[1]])
        if left_move_valid:
            # print("left")
            if height == "a":
                steps = 0
            pq.put((steps + 1, (left_loc)))
