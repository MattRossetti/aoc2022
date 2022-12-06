with open("input.txt") as file:
    input = file.read()

    received_chars = ""
    found = False
    for i, char in enumerate(input):
        if i == len(input) - 4:
            break
        packet = ""
        for j in range(4):
            if input[i + j] not in packet:
                packet += input[i + j]
            if len(packet) == 4:
                received_chars = i + j + 1
                found = True
        if found:
            break

answer = received_chars
print("answer:", answer)
