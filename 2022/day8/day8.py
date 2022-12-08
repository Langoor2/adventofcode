with open("input") as file:
     lines = [item.strip() for item in file.readlines()]

visible = 0
highest = 0
trees = []
verticaltrees = []
filewidth = len(lines)


for line in lines:
    treerow = []
    for tree in line:
        treerow.append([int(tree), visible])
    trees.append(treerow)

for treerow in trees:
    highest = -1
    for item in treerow:
        if item[0] > highest:
            visible +=1
            item[1] = 1
            highest = item[0]

for treerow in trees:
    highest = -1
    for item in treerow[::-1]:
        if item[0] > highest:
            if item[1] != 1:
                visible +=1
                item[1] = 1
            highest = item[0]


for i in range(len(trees[0])):
    row = []
    for j in trees:
        row.append(j[i])
    verticaltrees.append(row)


for treerow in verticaltrees:
    highest = -1
    for item in treerow:
        if item[0] > highest:
            if item[1] != 1:
                visible +=1
                item[1] = 1
            highest = item[0]

for treerow in verticaltrees:
    highest = -1
    for item in treerow[::-1]:
        if item[0] > highest:
            if item[1] != 1:
                visible +=1
                item[1] = 1
            highest = item[0]

print(visible)
