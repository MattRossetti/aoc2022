import copy


with open("input.txt") as file:
    lines = file.read().splitlines()
    instructions = []
    for line in lines:
        line = line.split()
        op = line[0]
        try:
            value = int(line[1])
        except IndexError:
            value = None
        instructions.append((op, value))


clean_instructions = []
for instruction in instructions:
    if instruction[0] == "noop":
        clean_instructions.append(("noop", 0))
        continue
    clean_instructions.append(("addx", 0))
    clean_instructions.append(instruction)

cycle = 0
x_value = 1
signals = set()
dark_row = ["." for _ in range(40)]
lines = []
for _ in range(6):
    lines.append(copy.copy(dark_row))
line_index = 0

for instruction in clean_instructions:
    p0 = x_value - 1
    p1 = x_value
    p2 = x_value + 1
    pixel_loc = [p0, p1, p2]
    for i in pixel_loc:
        if i == cycle:
            lines[line_index][cycle] = "#"
            break
    cycle += 1
    x_value += instruction[1]
    if cycle == 40:
        line_index += 1
        cycle = 0

for line in lines:
    print_str = ""
    for char in line:
        print_str += char
    print(print_str)
