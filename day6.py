with open("input6.txt") as f:
    points = [list(map(int, s.split(","))) for s in f.readlines()]

minx = min([p[0] for p in points])
miny = min([p[1] for p in points])
maxx = max([p[0] for p in points])
maxy = max([p[1] for p in points])

tdist = lambda x, y: sum([abs(x-p[0]) + abs(y-p[1]) for p in points])

def closest(x,y):
    mindist = abs(points[0][0]-x) + abs(points[0][1]-y)
    mini = 0
    doubled = False
    for (i, (px, py)) in enumerate(points):
        if i == 0:
            continue
        d = abs(x - px) + abs(y - py)
        if d < mindist:
            mini = i
            mindist = d
            doubled = False
        elif d == mindist:
            doubled = True
    if not doubled:
        return mini
    else:
        return None

area = [0 for _ in range(len(points))]
inf = [False for _ in range(len(points))]


for x in range(minx,maxx+1):
    ci = closest(x, miny)
    if ci:
        inf[ci] = True
    ci = closest(x, maxy)
    if ci:
        inf[ci] = True

for y in range(miny+1, maxy):
    ci = closest(minx, y)
    if ci:
        inf[ci] = True
    ci = closest(maxx, y)
    if ci:
        inf[ci] = True

for y in range(miny + 1, maxy):
    for x in range(minx + 1, maxx):
        ci = closest(x,y)
        if ci:
            if not inf[ci]:
                area[ci] += 1

maxp = max(range(len(points)), key = lambda x: area[x])

print(points[maxp], area[maxp])

# part 2
region = 0
for y in range(miny, maxy + 1):
    for x in range(minx, maxx + 1):
        if tdist(x,y) < 10000:
            region += 1
print(region)