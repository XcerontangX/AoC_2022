import day1part1

top3_total = 0

largest_sum = day1part1.largest_sum
calories_sum_list = list(day1part1.master_sum_list)
print(calories_sum_list)
largest_calories_sum_list = list([calories_sum_list[0], calories_sum_list[1], calories_sum_list[2]])
largest_calories_sum_list = list(enumerate(largest_calories_sum_list))
largest_calories_sum_list_2 = []
for indexed_item in largest_calories_sum_list:
    indexed_item = list(indexed_item)
    largest_calories_sum_list_2.append(indexed_item)
print(largest_calories_sum_list_2)

for current_sum in calories_sum_list:
    for index, largest_calories in largest_calories_sum_list_2:
        if current_sum > largest_calories:
            if index != 2:
                largest_calories_sum_list_2[index+1][1] = largest_calories_sum_list_2[index][1]
            largest_calories_sum_list_2[index][1] = current_sum
            print(largest_calories_sum_list_2)
            break

print(largest_calories_sum_list_2)
for index, calories in largest_calories_sum_list_2:
    top3_total += calories

print(top3_total)