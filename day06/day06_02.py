with open("input.txt") as file:
    input = file.read()

    received_chars = ""
    found = False
    for i, char in enumerate(input):
        if i == len(input) - 14:
            break
        packet = ""
        for j in range(14):
            if input[i + j] not in packet:
                packet += input[i + j]
            if len(packet) == 14:
                received_chars = i + j + 1
                found = True
        if found:
            break

answer = received_chars
print("answer:", answer)
