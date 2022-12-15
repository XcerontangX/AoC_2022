input = open(r"input\input_day5.txt", "r")
lines = input.readlines()

def Initialise():
    stack = []
    for i in lines:
        row = []
        i = i.replace("\n", "")
        i = [*i]
        if i[1] == '1':
            break
        for j in range(1, 35, 4):
            row.append(i[j])
        stack.append(row)
    stack = [list(k) for k in zip(*stack)]
    stack_filtered = []
    for s in stack:
        if " " in s:
            s = list(filter(lambda c: c != " ", s))
            stack_filtered.append(s)
        else:
            stack_filtered.append(s)
    return stack_filtered

def Update(line, stack):
    line = line.split()
    print(line)
    n = int(line[1])
    origin = int(line[3]) - 1
    destination = int(line[5]) - 1
    for i in range (0, n):
        item = stack[origin].pop(0)
        stack[destination].insert(0, item)
        print(item)

stack_live = Initialise()
print(stack_live)
instruction = "N"

for line in lines:
    line = line.replace("\n", "")
    if line == "":
        instruction = "Y"
        continue
    if instruction == "N":
        continue
    Update(line, stack_live)

answer = "".join([s[0] for s in stack_live])
print(answer)