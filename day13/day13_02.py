import ast
from queue import PriorityQueue


with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    packets = []
    for line in lines:
        if line == "":
            continue
        packets.append(ast.literal_eval(line))


def is_ordered(left, right):
    if left == [] and right != []:
        return True
    # print("comparing", left, "\n", "TO", right)
    ordered = None
    for i, left_val in enumerate(left):
        try:
            right_val = right[i]
        except IndexError:
            # right side is shorter
            # print("right ran out of items, false")
            return False
        # if both are ints
        if left_val == [] and right_val != []:
            # print("left empty, correct")
            return True
        if type(left_val) is int and type(right_val) is int:
            # print("comparing", left_val, right_val)
            if left_val != right_val:
                if left_val < right_val:
                    # print("left smaller, correct")
                    return True
                # print("right smaller, false")
                return False
        # if left is int and right is list
        if type(left_val) is int and type(right_val) is list:
            ordered = is_ordered([left_val], right_val)
            if ordered is not None:
                return ordered
        # if left is list and right is int
        if type(left_val) is list and type(right_val) is int:
            ordered = is_ordered(left_val, [right_val])
            if ordered is not None:
                return ordered
        # if both are lists
        if type(left_val) is list and type(right_val) is list:
            ordered = is_ordered(left_val, right_val)
            if ordered is not None:
                return ordered
        if i == len(left) - 1:
            try:
                right[i + 1]
                return True
            except IndexError:
                return False


packets.append([[2]])
packets.append([[6]])
sorted_packets = []
p_dict = dict()


def update_p_dict(count, p_dict):
    if count in p_dict:
        return update_p_dict(count + 1, p_dict)
    p_dict.update({count: p1})
    return p_dict


for p1 in packets:
    count = 0
    for p2 in packets:
        if p1 == p2:
            continue
        if is_ordered(p1, p2):
            count += 1
    p_dict = update_p_dict(count, p_dict)

for k, v in sorted(p_dict.items(), reverse=True):
    # print(len(p_dict) - k, v)
    if v == [[2]]:
        index_1 = len(p_dict) - k
    if v == [[6]]:
        index_2 = len(p_dict) - k

answer = index_1 * index_2
print("answer:", answer)
