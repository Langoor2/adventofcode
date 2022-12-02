with open("input") as file:
     lines = [item.strip() for item in file.readlines()]

totalscore = gamescore = 0

for line in lines:
    p1play, p2play = line.split(" ")
    if p2play == "X":
        gamescore = 1
        if p1play == "A":
            gamescore += 3
        elif p1play == "C":
            gamescore += 6
    elif p2play == "Y":
        gamescore = 2
        if p1play == "B":
            gamescore += 3
        elif p1play == "A":
            gamescore += 6
    elif p2play == "Z":
        gamescore = 3
        if p1play == "C":
            gamescore += 3
        elif p1play == "B":
            gamescore += 6
    totalscore += gamescore

print (totalscore)

# part 2
totalscore = 0

for line in lines:
    p1play, p2play = line.split(" ")
    if p2play == "X":
        gamescore = 0
        if p1play == "A":
            gamescore += 3
        elif p1play == "B":
            gamescore += 1
        elif p1play == "C":
            gamescore += 2
    elif p2play == "Y":
        gamescore = 3
        if p1play == "A":
            gamescore += 1
        elif p1play == "B":
            gamescore += 2
        elif p1play == "C":
            gamescore += 3
    elif p2play == "Z":
        gamescore = 6
        if p1play == "A":
            gamescore += 2
        elif p1play == "B":
            gamescore += 3
        elif p1play == "C":
            gamescore += 1
    totalscore += gamescore
print (totalscore)
