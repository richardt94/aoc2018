points = []
with open("input25.txt") as f:
    for pointln in f:
        x,y,z,w = map(int, pointln.split(","))
        points.append((x,y,z,w))

d = lambda p1, p2: sum(abs(p1[i] - p2[i]) for i in range(4))

constellations = []
for p1 in points:
    cis = []
    for i, c in enumerate(constellations):
        for p2 in c:
            if d(p1,p2) <= 3:
                cis.append(i)
                break
    newcs = []
    union = []
    for i, c in enumerate(constellations):
        if i in cis:
            union.extend(c)
        else:
            newcs.append(c)
    union.append(p1)
    newcs.append(union)
    constellations = newcs

print(len(constellations))
