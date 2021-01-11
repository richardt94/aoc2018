import re

with open("input10.txt") as f:
    pv = f.readlines()

prgx = re.compile(r"position=<([- 0-9]+), ([- 0-9]+)> velocity=<([- 0-9]+), ([- 0-9]+)>")
r = []
v = []
for point in pv:
    m = prgx.match(point)
    if not m:
        continue
    x, y, vx, vy = tuple(map(int, [m.group(i) for i in range(1,5)]))
    r.append((x,y))
    v.append((vx,vy))

maxx = max([p[0] for p in r])
minx = min([p[0] for p in r])
odx = maxx - minx
t = 0
#simulate till the points start drifting apart again
while maxx - minx <= odx:
    odx = maxx - minx
    t += 1
    for i, (x,y) in enumerate(r):
        r[i] = (x + v[i][0], y + v[i][1])
    maxx = max([p[0] for p in r])
    minx = min([p[0] for p in r])

#reverse one step
for i, (x,y) in enumerate(r):
    r[i] = (x - v[i][0], y - v[i][1])
maxx = max([p[0] for p in r])
minx = min([p[0] for p in r])
maxy = max([p[1] for p in r])
miny = min([p[1] for p in r])

print(t - 1)
for y in range(miny,maxy+1):
    scanline = ""
    for x in range(minx,maxx+1):
        if (x,y) in r:
            scanline += "#"
        else:
            scanline += " "
    print(scanline)
