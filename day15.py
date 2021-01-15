from collections import deque
from time import sleep

def display(dungeon, units):
    for y, l in enumerate(dungeon):
        scanl = ""
        for x, w in enumerate(l):
            if (y,x) in units:
                if units[(y,x)][0]:
                    scanl += 'G'
                else:
                    scanl += 'E'
            elif w:
                scanl += '#'
            else:
                scanl += '.'
        print(scanl)
    print()

with open("input15.txt") as f:
    dmap = [l.strip() for l in f.readlines()]
units = dict()
dungeon = []
for y, l in enumerate(dmap):
    dl = []
    for x, ch in enumerate(l):
        if ch == 'E':
            units[(y,x)] = (0,200)
        elif ch == 'G':
            units[(y,x)] = (1,200)
        elif ch == '#':
            dl.append(True)
            continue
        dl.append(False)
    dungeon.append(dl)

nsteps = 3
maxdist = len(dungeon) * len(dungeon[0])
for _ in range(60):
    upos = list(units.keys())
    upos.sort()
    for up in upos:
        #have i been killed?
        if up not in units:
            continue
        #move (bfs)
        mind = maxdist
        dist = {up:0}
        parents = dict()
        q = deque([up])
        closest = set()
        while len(q) > 0:
            y, x = q.popleft()
            d = dist[(y,x)]
            if d > mind:
                break
            for direc in range(4):
                ny = y + (direc == 3) - (direc == 0)
                nx = x + (direc == 2) - (direc == 1)
                if dungeon[ny][nx]:
                    continue
                if (ny, nx) in units:
                    if units[(ny, nx)][0] == 1 - units[up][0]:
                        mind = d
                        closest.add((y,x))
                    continue
                if (ny, nx) in dist:
                    if d + 1 == dist[(ny,nx)]:
                        parents[(ny,nx)].append((y,x))
                else:
                    dist[(ny,nx)] = d + 1
                    parents[(ny,nx)] = [(y,x)]
                    q.append((ny,nx))
        #only move if distance is nonzero and an in-range tile
        #was reachable
        if mind and len(closest):
            q = deque([min(closest)])
            mp = (len(dungeon), len(dungeon[0]))
            while len(q):
                p = q.popleft()
                for np in parents[p]:
                    if np == up:
                        if p < mp:
                            mp = p
                    else:
                        q.append(np)
            ustat = units[up]
            del units[up]
            units[mp] = ustat
            up = mp

        #attack if in range
        minhp = 201
        inr = False
        enemy = (0,0)
        for direc in range(4):
            ey = up[0] + (direc == 3) - (direc == 0)
            ex = up[1] + (direc == 2) - (direc == 1)
            if (ey, ex) in units:
                estats = units[(ey,ex)]
                if estats[0] == 1 - units[up][0] and estats[1] < minhp:
                    minhp = estats[1]
                    enemy = (ey,ex)
                    inr = True
        if inr:
            estats = units[enemy]
            if estats[1] < 3:
                del units[enemy]
            else:
                units[enemy] = (estats[0], estats[1] - 3)
    display(dungeon, units)
    sleep(0.5)

