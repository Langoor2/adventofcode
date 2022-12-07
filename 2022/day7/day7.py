from collections import OrderedDict
with open("test") as file:
     lines = [item.strip() for item in file.readlines()]

folderindex = dict()
subfolderindex = dict()
level = 0
folder = ""
size=0
subfolder = ""
totalsize = 0

for line in lines:
     if line == "$ cd /":
          folder = "/"
          level = 0
     elif line == "$ cd ..":
          totalsize = 0
          folder = ""
          level -= 1
     elif ("$ cd") in line:
          totalsize = 0
          level += 1
          folder = line.split("$ cd ", 1)[1]
     elif line == "$ ls":
          totalsize=0
     elif line.partition(" ")[0] == "dir":
          if folder not in folderindex:
               folderindex[folder]=0
          subfolder = line.split("dir ",1)[1]
          if folder not in subfolderindex:
               subfolderindex[folder] = list()
          subfolderindex[folder].append(subfolder)
     else:
          size = int(line.partition(" ")[0])
          totalsize += size
          folderindex[folder] = totalsize
          print(folder, size)

print(folderindex)
print(subfolderindex)
subfolderindex = OrderedDict(reversed(list(subfolderindex.items())))

for key,val in subfolderindex.items():
     for folder in val:
          folderindex[key] += folderindex[folder]
returnsize = 0
for key,val in folderindex.items():
     if val <=100000:
          print(val)
          returnsize += val
print(returnsize)
