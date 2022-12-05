with open("input.txt") as file:
    lines = file.read().splitlines()
    parsing_moves = False
    containers = [[] for _ in range(int((len(lines[0]) + 1) / 4))]
    # moves structure [0] = move count, [1] = from, [2] = to
    moves = []
    for line in lines:
        if not parsing_moves:
            if line == "":
                parsing_moves = True
                continue
            # skip container id row
            if line[1].isdigit():
                continue
            count = 0
            for i, char in enumerate(line):
                if char.isalpha():
                    id = i // 4
                    containers[id].insert(0, char)
                    count += 1
        else:
            line = line.split(" ")
            moves.append((int(line[1]), int(line[3]), int(line[5])))

for move in moves:
    count = move[0]
    from_id = move[1] - 1
    to_id = move[2] - 1
    popped = containers[from_id][count * -1:]
    containers[from_id] = containers[from_id][:count * -1]
    for char in popped:
        containers[to_id].append(char)

answer = ""
for container in containers:
    answer += container[-1]

print("answer")
print(answer)
