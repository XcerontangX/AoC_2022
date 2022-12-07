input = open("input\input_day3.txt", "r")

def Caluculate_Priorities (common_item_type):
    if common_item_type.isupper():
        priority = ord(common_item_type) - 38
    else:
        priority = ord(common_item_type) - 96
    print(priority)
    return priority

total = 0
elf_counter = 0
group_list_local = []
group_list_master = []

for i in input:
    i = i.replace("\n", "")
    group_list_local.append([*i])
    elf_counter += 1
    if elf_counter == 3:
        #print(group_list_local)
        group_list_master.append(group_list_local)
        elf_counter = 0
        group_list_local = []
        continue

for rucksack_list in group_list_master:
    print(rucksack_list)
    for rucksack in rucksack_list:
        for item in rucksack:
            if (item in rucksack_list[1]) and (item in rucksack_list[2]):
                print(item)
                priority_item = Caluculate_Priorities(item)
                total += priority_item
                break
        break

print(total)

