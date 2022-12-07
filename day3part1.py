input = open("input\input_day3.txt", "r")

def Caluculate_Priorities (common_item_type):
    if common_item_type.isupper():
        priority = ord(common_item_type) - 38
    else:
        priority = ord(common_item_type) - 96
    print(priority)
    return priority

total = 0

for i in input:
    i = i.replace("\n", "")
    item_list = [*i]
    comp1_list = item_list[:int(len(item_list)/2)]
    comp2_list = item_list[int(len(item_list)/2):]
    print(comp1_list, comp2_list)
    for comp1_item in comp1_list:
        if comp1_item in comp2_list:
            common_item_type = comp1_item
            break
    priority_item = Caluculate_Priorities(common_item_type)
    total += priority_item

print(total)