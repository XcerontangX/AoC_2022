input = open("input\input_day2.txt", "r")

def Calculate_Score (opponent_pick, my_pick):
    sum = 0
    RPS_list = [[0,"AX"], [1, "BY"], [2, "CZ"]]
    for j, RPS_letter in RPS_list:
        if opponent_pick in RPS_letter:
            opponent_pick_index = j
        if my_pick in RPS_letter:
            my_pick_index = j
            sum += (j+1)
    print (opponent_pick, my_pick, opponent_pick_index, my_pick_index)
    if opponent_pick_index == my_pick_index:
        sum += 3
    if (my_pick_index - opponent_pick_index) == 1 or (my_pick_index - opponent_pick_index) == -2:
        sum += 6
    print(sum)
    return sum

total_score = 0

for i in input:
    i = i.replace("\n", "")
    strategy_list = i.split()
    opponent_pick = strategy_list[0]
    my_pick = strategy_list[1]
    score = Calculate_Score(opponent_pick, my_pick)
    total_score += score

print(total_score)