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


def move_tail(step, head_location, tail_location):
    distance_between = find_distance_between(head_location, tail_location)
    # dist between [0,0] and [1,1] = ~1.41
    if distance_between > 1.42:
        if step[0] == "U":
            tail_location[0] = head_location[0]
            tail_location[1] = head_location[1] - 1
        if step[0] == "R":
            tail_location[0] = head_location[0] - 1
            tail_location[1] = head_location[1]
        if step[0] == "D":
            tail_location[0] = head_location[0]
            tail_location[1] = head_location[1] + 1
        if step[0] == "L":
            tail_location[0] = head_location[0] + 1
            tail_location[1] = head_location[1]
    return tail_location


head_location = [0, 0]
tail_location = [0, 0]
tail_visited = {tuple(tail_location)}

for move in moves:
    for _ in range(move[1]):
        step = (move[0], 1)
        head_location = move_head(step, head_location)
        # print("head:", head_location)
        tail_location = move_tail(step, head_location, tail_location)
        tail_visited.add(tuple(tail_location))
        # print("tail:", tail_location)
        # print()

answer = len(tail_visited)
print("answer: ", answer)
