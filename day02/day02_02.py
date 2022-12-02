with open("input.txt", 'r') as file:
    rounds = file.read().splitlines()


score_dict = {"X": 1, "Y": 2, "Z": 3}
result_score_dict = {"X": 0, "Y": 3, "Z": 6}
win_dict = {"A": "Y", "B": "Z", "C": "X"}
lose_dict = {"A": "Z", "B": "X", "C": "Y"}
draw_dict = {"A": "X", "B": "Y", "C": "Z"}


score = 0
for round in rounds:
    opponent_move = round[0]
    result = round[2]
    score += result_score_dict[result]
    if result == "X":
        my_move = lose_dict[opponent_move]
    if result == "Y":
        my_move = draw_dict[opponent_move]
    if result == "Z":
        my_move = win_dict[opponent_move]
    score += score_dict[my_move]

answer = score
print(answer)
