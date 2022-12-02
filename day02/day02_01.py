with open("input.txt", 'r') as file:
    rounds = file.read().splitlines()


score_dict = {"X": 1, "Y": 2, "Z": 3}
win_dict = {"A": "Y", "B": "Z", "C": "X"}
match_dict = {"A": "X", "B": "Y", "C": "Z"}


score = 0
for round in rounds:
    opponent_move = round[0]
    my_move = round[2]
    score += score_dict[my_move]
    if win_dict[opponent_move] == my_move:
        score += 6
    if match_dict[opponent_move] == my_move:
        score += 3

answer = score
print(answer)
