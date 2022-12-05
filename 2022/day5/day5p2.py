with open ("input") as file:
    lines = [item.strip() for item in file.readlines()]

parsedstarting = False

stacks = dict()
stack1 = []
stack2 = []
stack3 = []
stack4 = []
stack5 = []
stack6 = []
stack7 = []
stack8 = []
stack9 = []
stacks[1] = stack1
stacks[2] = stack2
stacks[3] = stack3
stacks[4] = stack4
stacks[5] = stack5
stacks[6] = stack6
stacks[7] = stack7
stacks[8] = stack8
stacks[9] = stack9

for line in lines:
    if line.startswith("1 "):
        parsedstarting = True
    elif parsedstarting == False:
        items = int((len(line)+1)/4)
        if items >= 1 and line[1] != " ":
            stacks[1].append(line[1])
        if items >= 2 and line[5] != " ":
            stacks[2].append(line[5])
        if items >= 3 and line[9] != " ":
            stacks[3].append(line[9])
        if items >= 4 and line[13] != " ":
            stacks[4].append(line[13])
        if items >= 5 and line[17] != " ":
            stacks[5].append(line[17])
        if items >= 6 and line[21] != " ":
            stacks[6].append(line[21])
        if items >= 7 and line[25] != " ":
            stacks[7].append(line[25])
        if items >= 8 and line[29] != " ":
            stacks[8].append(line[29])
        if items >= 9 and line[33] != " ":
            stacks[9].append(line[33])
    elif parsedstarting == True and line.startswith("move"):
        amount = line[5]
        if line[6] != " ":
            amount = amount+line[6]
        amount = int(amount)
        dest = int(line[len(line)-1])
        org = int(line[line.rfind("m")+2])
        boxes = ""
        while amount != 0:
            item = stacks[org][0]
            stacks[org].pop(0)
            boxes = boxes + item
            amount -= 1
        for box in boxes[::-1]:
            stacks[dest].insert(0, box)

ansstr = ""
for ans in range(9):
    ansstr = ansstr + stacks[ans+1][0]
print (ansstr)
