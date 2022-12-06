with open("input") as file:
     lines = [item.strip() for item in file.readlines()]

pos=0
packets=[]
firstpos = 0
firstset = False

for line in lines:
     for char in line:
          pos += 1
          if len(packets) < 4:
               packets.append(char)
          else:
               if (len(packets)==len(set(packets))) == True:
                    if firstset == False:
                         firstset = True
                         firstpos = pos
               packets.pop(0)
               packets.append(char)
print (firstpos-1)


pos=0
packets=[]
firstpos = 0
firstset = False

for line in lines:
     for char in line:
          pos += 1
          if len(packets) < 14:
               packets.append(char)
          else:
               if (len(packets)==len(set(packets))) == True:
                    if firstset == False:
                         firstset = True
                         firstpos = pos
               packets.pop(0)
               packets.append(char)
print (firstpos-1)

