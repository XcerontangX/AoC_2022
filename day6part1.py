input = open(r"input\input_day6.txt", "r")
data_raw = [*str(input.readlines()[0])]
data_raw = list(enumerate(data_raw))
print(data_raw)

def allUnique(check_list):
    print(check_list)
    seen = set()
    return not any(i in seen or seen.add(i) for i in check_list)

check_list = []
unique_list = []
for index, char in data_raw:
    if index < 3:
        continue
    for i in range (0, 4):
        check_list.append(data_raw[index - (3 - i)][1])
    unique = allUnique(check_list)
    print(unique, index + 1)
    unique_list.append(unique)
    check_list = []

print(unique_list)

counter = 4
for item in unique_list:
    if item is not True:
        counter += 1
        continue
    break
    
print(counter)
