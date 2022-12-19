import ast


with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    packets = []
    pair = []
    for line in lines:
        if line == "":
            packets.append(pair)
            pair = []
            continue
        pair.append(ast.literal_eval(line))
    packets.append(pair)


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


def solve(packets):
    count = 1
    ordered_indexes = []
    for pair in packets:
        # print(f"== Pair {count} ==")
        left = pair[0]
        right = pair[1]
        if is_ordered(left, right):
            ordered_indexes.append(count)
        count += 1
        # print()
    return ordered_indexes


ordered_pairs = solve(packets)
print(ordered_pairs)
answer = sum(ordered_pairs)
print("answer:", answer)
