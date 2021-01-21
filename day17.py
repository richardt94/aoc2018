import re
import sys
sys.setrecursionlimit(2000)

with open("input17.txt") as f:
    blocks = f.readlines()

blockrgx = re.compile(r"(y|x)=([0-9]+), (y|x)=([0-9]+)\.\.([0-9]+)")
blocked = set()
for block in blocks:
    m = blockrgx.match(block)
    if not m:
        continue
    vert = m.group(1) == "x"
    fixed = int(m.group(2))
    v0 = int(m.group(4))
    v1 = int(m.group(5))
    for var in range(v0,v1+1):
        if vert:
            blocked.add((fixed,var))
        else:
            blocked.add((var,fixed))

def display(blocked, visited, filled):
    minx = min(blocked, key = lambda x: x[0])[0]
    miny = min(blocked, key = lambda x: x[1])[1]
    maxx = max(blocked, key = lambda x: x[0])[0]
    maxy = max(blocked, key = lambda x: x[1])[1]
    for y in range(miny, maxy + 1):
        scanline = ""
        for x in range(minx, maxx + 1):
            if (x, y) in blocked:
                scanline += "#"
            elif (x,y) in filled:
                scanline += "~"
            elif (x,y) in visited:
                scanline += "|"
            else:
                scanline += "."
        print(scanline)

filled = set()
visited = set()
maxy = max(blocked, key = lambda x: x[1])[1]
miny = min(blocked, key = lambda x: x[1])[1]
def vertflow(x,y):
    if y > maxy:
        return
    visited.add((x,y))
    if (x,y+1) not in blocked and (x,y+1) not in visited:
        vertflow(x,y+1)

    if (x,y+1) in blocked or (x,y+1) in filled:
        #spread
        hvis = set()
        leak = False
        nx = x-1
        while (nx,y) not in visited and (nx,y) not in blocked:
            hvis.add((nx,y))
            visited.add((nx,y))
            if (nx,y+1) not in blocked:
                if (nx,y+1) not in visited:
                    vertflow(nx,y+1)
                if (nx,y+1) not in filled:
                    leak = True
                    break
            nx -= 1
        nx = x+1
        while (nx,y) not in visited and (nx,y) not in blocked:
            hvis.add((nx,y))
            visited.add((nx,y))
            if (nx,y+1) not in blocked:
                if (nx,y+1) not in visited:
                    vertflow(nx,y+1)
                if (nx,y+1) not in filled:
                    leak = True
                    break
            nx += 1
        if not leak:
            [filled.add(pt) for pt in hvis]
            filled.add((x,y))


vertflow(500,miny)
display(blocked, visited, filled)
print(len(visited), len(filled))