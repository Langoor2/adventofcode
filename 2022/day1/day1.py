file1 = open('input', 'r')
Lines = file1.readlines()

calories = 0
count = 0
elves = []

for line in Lines:
    count += 1
    if line.strip():
        #print(count, line.strip())
        calories = calories + int(line)
        print (line.strip())
    if not line.strip():
        elves.append(calories)
        calories = 0

elves.sort()

print(elves)
print (elves[len(elves)-1])
top3 = elves[len(elves)-1] + elves[len(elves)-2] + elves[len(elves) -3 ]
print (top3)
