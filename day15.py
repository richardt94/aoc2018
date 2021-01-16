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

direcs = [(0,1), (1,0), (-1,0), (0,-1)]
def findmove(dungeon, units, spos):
    #squares in range
    etype = 1 - units[spos][0]
    inr = set()
    for u in units.items():
        if u[1][0] == etype:
            for dr in direcs:
                inr.add((u[0][0] + dr[0], u[0][1] + dr[1]))

    occupied = {u for u in units}
    #store only the first-reading-order
    #parent to each point in par
    par = {spos:(0,None)}
    visited = set()
    q = deque([(spos,0)])
    while q:
        pos, dist = q.popleft()
        for dr in direcs:
            npos = (pos[0] + dr[0], pos[1] + dr[1])
            if dungeon[npos[0]][npos[1]] or npos in occupied:
                continue
            if npos not in par or par[npos] > (dist + 1, pos):
                par[npos] = (dist + 1, pos)
            if npos in visited:
                continue
            if not any(npos == el[0] for el in q):
                q.append((npos,dist + 1))
        visited.add(pos)
    try:
        _, closest = min((dist,pos) for pos, (dist,_) in par.items() if pos in inr)
    except ValueError: #no reachable squares in range of an enemy
        return

    while par[closest][0] > 1:
        closest = par[closest][1]

    return closest


with open("input15.txt") as f:
    dmap = [l.strip() for l in f.readlines()]
units = dict()
dungeon = []
nu = [0,0]
for y, l in enumerate(dmap):
    dl = []
    for x, ch in enumerate(l):
        if ch == 'E':
            units[(y,x)] = (0,200)
            nu[0] += 1
        elif ch == 'G':
            units[(y,x)] = (1,200)
            nu[1] += 1
        elif ch == '#':
            dl.append(True)
            continue
        dl.append(False)
    dungeon.append(dl)

done = False
nrounds = 0
while True:
    upos = list(units.keys())
    upos.sort()
    for up in upos:
        #have i been killed?
        if up not in units:
            continue
        etype = 1 - units[up][0]
        if not nu[etype]:
            done = True
            break
        #move
        moveto = findmove(dungeon, units, up)
        if moveto:
            ustats = units[up]
            del units[up]
            units[moveto] = ustats
            up = moveto

        #attack if in range
        adj = []
        for dr in direcs:
            epos = (up[0] + dr[0], up[1] + dr[1])
            if epos in units and units[epos][0] == etype:
                adj.append((units[epos][1], epos))
        if adj:
            ehp, epos = min(adj)
            if ehp <= 3:
                del units[epos]
                nu[etype] -= 1
            else:
                units[epos] = (etype, ehp - 3)

    display(dungeon, units)
    if done:
        break
    nrounds += 1

print(nrounds)
thp = sum(u[1] for u in units.values())
print(thp)
print(thp*nrounds)
