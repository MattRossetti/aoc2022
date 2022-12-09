import math


with open("input.txt") as file:
    lines = file.read().splitlines()
    moves = []
    for line in lines:
        direction = line[0]
        steps = int(line[2:])
        moves.append((direction, steps))


def move_head(move, head_location):
    if move[0] == "U":
        head_location[1] += move[1]
    if move[0] == "R":
        head_location[0] += move[1]
    if move[0] == "D":
        head_location[1] -= move[1]
    if move[0] == "L":
        head_location[0] -= move[1]
    return head_location


def find_distance_between(head_location, tail_location):
    x_dist_squared = pow(head_location[0] - tail_location[0], 2)
    y_dist_squared = pow(head_location[1] - tail_location[1], 2)
    distance_between = math.sqrt(x_dist_squared + y_dist_squared)
    return distance_between


def move_tail(step, head_loc, tail_loc):
    distance_between = find_distance_between(head_loc, tail_loc)
    # dist between [0,0] and [1,1] = ~1.41
    if distance_between > 1.42:
        # up
        if head_loc[0] == tail_loc[0] and head_loc[1] > tail_loc[1]:
            tail_loc[1] += 1
        # right
        if head_loc[1] == tail_loc[1] and head_loc[0] > tail_loc[0]:
            tail_loc[0] += 1
        # down
        if head_loc[0] == tail_loc[0] and head_loc[1] < tail_loc[1]:
            tail_loc[1] -= 1
        # left
        if head_loc[1] == tail_loc[1] and head_loc[0] < tail_loc[0]:
            tail_loc[0] -= 1
        # up_right
        if head_loc[0] > tail_loc[0] and head_loc[1] > tail_loc[1]:
            tail_loc[0] += 1
            tail_loc[1] += 1
        # down_right
        if head_loc[0] > tail_loc[0] and head_loc[1] < tail_loc[1]:
            tail_loc[0] += 1
            tail_loc[1] -= 1
        # down_left
        if head_loc[0] < tail_loc[0] and head_loc[1] < tail_loc[1]:
            tail_loc[0] -= 1
            tail_loc[1] -= 1
        # up_left
        if head_loc[0] < tail_loc[0] and head_loc[1] > tail_loc[1]:
            tail_loc[0] -= 1
            tail_loc[1] += 1
    return tail_loc


head_location = [0, 0]
t1_loc = [0, 0]
t2_loc = [0, 0]
t3_loc = [0, 0]
t4_loc = [0, 0]
t5_loc = [0, 0]
t6_loc = [0, 0]
t7_loc = [0, 0]
t8_loc = [0, 0]
t9_loc = [0, 0]
tail_visited = {tuple(t9_loc)}

for move in moves:
    # print(move)
    for _ in range(move[1]):
        step = (move[0], 1)
        head_location = move_head(step, head_location)
        t1_loc = move_tail(step, head_location, t1_loc)
        t2_loc = move_tail(step, t1_loc, t2_loc)
        t3_loc = move_tail(step, t2_loc, t3_loc)
        t4_loc = move_tail(step, t3_loc, t4_loc)
        t5_loc = move_tail(step, t4_loc, t5_loc)
        t6_loc = move_tail(step, t5_loc, t6_loc)
        t7_loc = move_tail(step, t6_loc, t7_loc)
        t8_loc = move_tail(step, t7_loc, t8_loc)
        t9_loc = move_tail(step, t8_loc, t9_loc)
        tail_visited.add(tuple(t9_loc))

answer = len(tail_visited)
print("answer: ", answer)
