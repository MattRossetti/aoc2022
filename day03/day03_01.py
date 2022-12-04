compartments = []
with open("input.txt") as file:
    lines = file.read().splitlines()
    for line in lines:
        half_length = int(len(line) / 2)
        first = line[0: half_length]
        second = line[half_length:]
        compartments.append([first, second])


priorities = []
for compartment in compartments:
    priority_found = False
    for char in compartment[0]:
        if char in compartment[1] and not priority_found:
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
