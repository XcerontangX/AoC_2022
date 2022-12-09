input = open("input\input_day4.txt", "r")

def InclusionTest (list):
    if (list[0] >= list[2] and list[1] <= list[3]) or (list[2] >= list[0] and list[3] <= list[1]):
        return True
    else:
        return False

counter = 0
lines = input.readlines()
for line in lines:
    line = line.replace("\n", "")
    elf_section_list = []
    for i in range (0, 2):
        for j in range (0, 2):
           elf_section_list.append(int(line.split(",")[i].split("-")[j]))
    print(elf_section_list)
    inclusion = InclusionTest(elf_section_list)
    print(inclusion)
    if inclusion is True:
        counter += 1
        continue

print(counter)
