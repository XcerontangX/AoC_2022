input = open("input\input_day1.txt", "r")
master_sum_list = []
sum = 0
for i in input:
    i = i.replace("\n", "")
    if i == "":
        print("SPACE", sum)
        master_sum_list.append(sum)
        sum = 0
        continue
    i = float(i)
    sum = sum + i
    print(i)

largest_sum = master_sum_list[0]
for current_sum in master_sum_list:
    if current_sum > largest_sum:
        largest_sum = current_sum

print(largest_sum)
