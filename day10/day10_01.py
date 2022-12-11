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

cycle = 1
x_value = 1
signals = set()
for instruction in instructions:
    if (cycle + 20) % 40 == 0:
        signals.add((cycle, x_value))
    if instruction[0] == "noop":
        cycle += 1
        continue
    for _ in range(2):
        if (cycle + 20) % 40 == 0:
            signals.add((cycle, x_value))
        cycle += 1
    x_value += instruction[1]

total_strength = 0
for signal in signals:
    signal_strength = signal[0] * signal[1]
    total_strength += signal_strength

print(total_strength)
