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
    overlaps = []
    # find overlaps from first
    for digit in pair[0]:
        if digit in pair[1] and digit not in overlaps:
            overlaps.append(digit)
    # find overlaps from second
    for digit in pair[1]:
        if digit in pair[0] and digit not in overlaps:
            overlaps.append(digit)
    if len(overlaps) != 0:
        count += 1

answer = count
print(count)
