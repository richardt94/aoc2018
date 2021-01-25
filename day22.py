import heapq

# testing
# depth = 510
# tx = 10
# ty = 10

# puzzle
depth = 6084
tx = 14
ty = 709

el = [[0 for _ in range(tx+1)] for _ in range(ty+1)]
for x in range(tx+1):
    el[0][x] = (x * 16807 + depth) % 20183
for y in range(1,ty+1):
    el[y][0] = (y * 48271 + depth) % 20183

for x in range(1,tx+1):
    for y in range(1,ty+1):
        if x == tx and y == ty:
            el[y][x] = depth % 20183
        else:
            el[y][x] = (el[y][x-1] * el[y-1][x] + depth) % 20183

for elr in el:
    scanline = ""
    for cellel in elr:
        if cellel % 3 == 0:
            scanline += "."
        elif cellel % 3 == 1:
            scanline += "="
        else:
            scanline += "|"
    print(scanline)

print(sum(sum(elc%3 for elc in elr) for elr in el))

eroded = dict()
for y, elr in enumerate(el):
    for x, elc in enumerate(elr):
        eroded[(x,y)] = elc

def getel(x,y):
    if (x,y) in eroded:
        return eroded[(x,y)]
    if x == 0:
        eroded[(x,y)] = (y * 48271 + depth) % 20183
    elif y == 0:
        eroded[(x,y)] = (x * 16807 + depth) % 20183
    else:
        eroded[(x,y)] = (getel(x,y-1)*getel(x-1,y) + depth) % 20183
    return eroded[(x,y)]

visited = set()

#nothing is zero, torch is 1, climbing gear is 2.
#this means that if the type of a cell is equal
#to the current tool, we can't go there without changing
tovisit = [(0,0,0,1)]
x = 0
y = 0
tool = 0
while (x, y, tool) != (tx, ty, 1):
    dist, x, y, tool = heapq.heappop(tovisit)
    if (x, y, tool) in visited:
        continue
    visited.add((x, y, tool))
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direc in dirs:
        nx, ny = x + direc[0], y + direc[1]
        if nx < 0 or ny < 0 or (nx, ny, tool) in visited:
            continue
        if getel(nx, ny) % 3 != tool:
            heapq.heappush(tovisit, (dist + 1, nx, ny, tool))
    for ti in range(1,3):
        nt = (tool + ti) % 3
        if nt != getel(x,y) % 3:
            heapq.heappush(tovisit, (dist + 7, x, y, nt))

print(dist)