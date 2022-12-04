with open ("input") as file:
    lines = [item.strip() for item in file.readlines()]

fullycontaincount = 0

for line in lines:
    elf1, elf2 = line.split(',')
    elf1l, elf1u = elf1.split('-')
    elf2l, elf2u = elf2.split('-')
    elf1 = set(range(int(elf1l), int(elf1u)+1))
    elf2 = set(range(int(elf2l), int(elf2u)+1))
    if elf1.issubset(elf2) or elf2.issubset(elf1):
        fullycontaincount += 1

print(fullycontaincount)

# Part2

overlapcount = 0

for line in lines:
    elf1, elf2 = line.split(',')
    elf1l, elf1u = elf1.split('-')
    elf2l, elf2u = elf2.split('-')
    elf1 = set(range(int(elf1l), int(elf1u)+1))
    elf2 = set(range(int(elf2l), int(elf2u)+1))
    if elf1.intersection(elf2) or elf2.intersection(elf1):
        overlapcount += 1

print(overlapcount)

