input = open("input\input_day2.txt", "r")

def Calculate_Score (opponent_pick, round_result):
    sum = 0
    RPS_list = ["A", "B", "C"]
    LDW_list = ["X", "Y", "Z"]
    for j, LDW in list(enumerate(LDW_list)):
        if round_result in LDW:
            sum += (j+2*j)
            for k, RPS_letter in list(enumerate(RPS_list)):
                if opponent_pick in RPS_letter:
                    opponent_pick_index = k
                    if j == 1:
                        sum += (k+1)
                        break
                    if j == 0:
                        if opponent_pick_index == 0:
                            my_pick_index = opponent_pick_index + 2
                        else:
                            my_pick_index = opponent_pick_index - 1
                        sum += (my_pick_index + 1)
                        break
                    if j == 2:
                        if opponent_pick_index == 2:
                            my_pick_index = opponent_pick_index - 2
                        else:
                            my_pick_index = opponent_pick_index + 1
                        sum += (my_pick_index + 1)
                        break
            break
    print(opponent_pick, round_result, sum)
    return sum

total_score = 0

for i in input:
    i = i.replace("\n", "")
    strategy_list = i.split()
    opponent_pick = strategy_list[0]
    round_result = strategy_list[1]
    score = Calculate_Score(opponent_pick, round_result)
    total_score += score

print(total_score)
