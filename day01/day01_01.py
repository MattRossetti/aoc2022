with open("input.txt") as file:
    lines = file.read().splitlines()
    calorie_list = []
    calories = 0
    for line in lines:
        if line == "":
            calorie_list.append(calories)
            calories = 0
            continue
        calories += int(line)

answer = max(calorie_list)
print(answer)
