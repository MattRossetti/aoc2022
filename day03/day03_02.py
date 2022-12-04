groups = []
with open("input.txt") as file:
    lines = file.read().splitlines()
    count = 0
    group = []
    for line in lines:
        group.append(line)
        count += 1
        if count % 3 == 0:
            groups.append(group)
            group = []


priorities = []
for group in groups:
    priority_found = False
    for char in group[0]:
        if char in group[1] and char in group[2] and not priority_found:
            priorities.append(char)
            priority_found = True


priorities_converted = []
for char in priorities:
    if char.islower():
        # ascii of "a" is 97
        converted = ord(char) - 96
    else:
        # ascii of "A" is 64
        # capitals come after lower case for puzzle
        converted = ord(char) - 64 + 26
    priorities_converted.append(converted)

answer = sum(priorities_converted)

print("answer")
print(answer)
