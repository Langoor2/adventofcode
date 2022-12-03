with open("input") as file:
     lines = [item.strip() for item in file.readlines()]

totalprio = 0

for line in lines:
	comp1, comp2 = line[:len(line)//2], line[len(line)//2:]
	comp1 = set(comp1)
	comp2 = set(comp2)
	shareditem = str(comp1.intersection(comp2))[2] # Is there a better way to do this??? (esp. the [2])
	if shareditem.islower():
		itemprio = ord(shareditem) - 96
	else:
		itemprio = ord(shareditem) - 38
	print(shareditem)
	print(itemprio)
	totalprio = totalprio + itemprio
	
print()
print(totalprio)

# part 2
totalprio = 0
elf1 = 0
elf2 = 0
elf3 = 0
i = 0

for line in lines:
	if i==0:
		elf1 = set(line)
		i += 1
	elif i==1:
		elf2 = set(line)
		i += 1
	elif i==2:
		elf3 = set(line)
		i = 0
		shareditem = str(elf1.intersection(elf2, elf3))[2]
		if shareditem.islower():
			itemprio = ord(shareditem) - 96
		else:
			itemprio = ord(shareditem) - 38
		totalprio = totalprio + itemprio
		print(shareditem)
		print(itemprio)
print()
print(totalprio)


