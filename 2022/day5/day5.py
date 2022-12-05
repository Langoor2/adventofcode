with open ("input") as file:
    lines = [item.strip() for item in file.readlines()]

parsedstarting = False

stacks = {stack: [] for stack in range(1, 10)}

for line in lines:
    if line.startswith("1 "):
        parsedstarting = True
    elif parsedstarting == False:
        items = int((len(line)+1)/4)
        for i in range(1, items+1):
            if items >= i and line[(i-1)*4+1] != " ":
                stacks[i].append(line[(i-1)*4+1])
    elif parsedstarting == True and line.startswith("move"):
        amount = line[5]
        if line[6] != " ":
            amount = amount+line[6]
        amount = int(amount)
        dest = int(line[len(line)-1])
        org = int(line[line.rfind("m")+2])

        while amount != 0:
            item = stacks[org][0]
            stacks[org].pop(0)
            stacks[dest].insert(0, item)
            amount -= 1

ansstr = ""
for ans in range(9):
    ansstr = ansstr + stacks[ans+1][0]
print (ansstr)

# part2

parsedstarting = False

stacks = {stack: [] for stack in range(1, 10)}

for line in lines:
    if line.startswith("1 "):
        parsedstarting = True
    elif parsedstarting == False:
        items = int((len(line)+1)/4)
        for i in range(1, items+1):
            if items >= i and line[(i-1)*4+1] != " ":
                stacks[i].append(line[(i-1)*4+1])
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
