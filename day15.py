from collections import deque

def display(dungeon, units):
    for y, l in enumerate(dungeon):
        scanl = ""
        for x, w in enumerate(l):
            for u in units:
                if (y,x) == u[0:2] and not u[4]:
                    if u[2]:
                        scanl += 'G'
                    else:
                        scanl += 'E'
                    break
            else:
                if w:
                    scanl += '#'
                else:
                    scanl += '.'
        print(scanl)
    print()

direcs = [(0,1), (1,0), (-1,0), (0,-1)]
def findmove(dungeon, units, su):
    #squares in range
    etype = 1 - su[2]
    inr = set()
    for u in units:
        if u[2] == etype and not u[4]:
            for dr in direcs:
                inr.add((u[0] + dr[0], u[1] + dr[1]))
    spos = (su[0], su[1])
    if (su[0], su[1]) in inr:
        return

    occupied = {(u[0], u[1]) for u in units if not u[4]}
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
unitsref = []
dungeon = []
nuref = [0,0]
for y, l in enumerate(dmap):
    dl = []
    for x, ch in enumerate(l):
        if ch == 'E':
            unitsref.append((y,x,0,200,False))
            nuref[0] += 1
        elif ch == 'G':
            unitsref.append((y,x,1,200,False))
            nuref[1] += 1
        elif ch == '#':
            dl.append(True)
            continue
        dl.append(False)
    dungeon.append(dl)

def playpower(power):
    units = unitsref.copy()
    nu = nuref.copy()
    done = False
    nrounds = 0
    while True:
        units.sort()
        for (ui,unit) in enumerate(units):
            #have i been killed?
            if unit[4]:
                continue
            etype = 1 - unit[2]
            if not nu[etype]:
                done = True
                break
            #move
            moveto = findmove(dungeon, units, unit)
            if moveto:
                units[ui] = (*moveto, *unit[2:])
                unit = units[ui]

            #attack if in range
            adj = []
            for dr in direcs:
                epos = (unit[0] + dr[0], unit[1] + dr[1])
                for i,u in enumerate(units):
                    if u[0:2] == epos and u[2] == etype and not u[4]:
                        adj.append((u[3],epos,i))

            if adj:
                ehp, epos, ei = min(adj)
                ehp -= (3 if etype == 0 else power)
                if ehp <= 0:
                    if etype == 0:
                        return 0
                    units[ei] = (*epos, etype, ehp, True)
                    nu[etype] -= 1
                else:
                    units[ei] = (*epos, etype, ehp, False)
        if done:
            break
        nrounds += 1

    thp = sum(u[3] for u in units if not u[4])
    
    return thp*nrounds

score = 0
power = 3
while score == 0:
    power += 1
    score = playpower(power)
print(power, score)
