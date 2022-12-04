with open("input.txt") as file:
    lines = file.read().splitlines()
    pairs = []
    for line in lines:
        line = line.split(",")
        line[0] = line[0].split("-")
        line[1] = line[1].split("-")
        first = [i for i in range(int(line[0][0]), int(line[0][1]) + 1)]
        second = [i for i in range(int(line[1][0]), int(line[1][1]) + 1)]
        pairs.append([first, second])

count = 0
for pair in pairs:
    # check if first pair contains second
    in_second = True
    for digit in pair[0]:
        if not in_second:
            continue
        if digit not in pair[1]:
            in_second = False
            continue
    if in_second:
        count += 1
        continue
    # check if second pair contains first
    in_first = True
    for digit in pair[1]:
        if not in_first:
            continue
        if digit not in pair[0]:
            in_first = False
            continue
    if in_first:
        count += 1

answer = count
print(count)
