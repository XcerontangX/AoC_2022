input = open("input\input_day4.txt", "r")

def OverlapTest (list):
    range1 = range(list[0], list[1]+ 1)
    range2 = range(list[2], list[3]+ 1)
    for value in range1:
        if value in range2:
            return True

counter = 0
lines = input.readlines()
for line in lines:
    line = line.replace("\n", "")
    elf_section_list = []
    for i in range (0, 2):
        for j in range (0, 2):
           elf_section_list.append(int(line.split(",")[i].split("-")[j]))
    print(elf_section_list)
    overlap = OverlapTest(elf_section_list)
    print(overlap)
    if overlap is True:
        counter += 1
        continue

print(counter)
