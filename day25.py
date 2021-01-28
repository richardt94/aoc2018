points = []
with open("input25.txt") as f:
    for pointln in f:
        x,y,z,w = map(int, pointln.split(","))
        points.append((x,y,z,w))

d = lambda p1, p2: sum(abs(p1[i] - p2[i]) for i in range(4))

uf = list(range(len(points)))

def find(i):
    path = []
    while uf[i] != i:
        path.append(i)
        i = uf[i]
    for i2 in path:
        uf[i2] = i
    return i

def union(i,j):
    uf[find(i)] = find(j)

for i, p1 in enumerate(points):
    for j, p2 in enumerate(points[i+1:]):
        if d(p1,p2) <= 3:
            union(i,i+1+j)

cons = set()
for i in range(len(points)):
    cons.add(find(i))
print(len(cons))
