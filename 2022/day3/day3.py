with open("test1") as file:
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

for line in lines:
	
