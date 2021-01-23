with open("input18.txt") as f:
    cstate = []
    for line in f:
        l = line.strip()
        if not l:
            continue
        lst = []
        for ch in l:
            if ch == '.':
                lst.append(0)
            elif ch == '#':
                lst.append(2)
            else:
                lst.append(1)
        cstate.append(lst)

def display(state):
    for row in state:
        scanline = ""
        for cell in row:
            if cell == 0:
                scanline += "."
            elif cell == 1:
                scanline += "|"
            else:
                scanline += "#"
        print(scanline)

def ntype(lt,y,x,cstate):
    nt = 0
    if y > 0 and cstate[y-1][x] == lt:
        nt += 1
    if y > 0 and x > 0 and cstate[y-1][x-1] == lt:
        nt += 1
    if y > 0 and x < len(cstate[0]) - 1 and cstate[y-1][x+1] == lt:
        nt += 1
    if x > 0 and cstate[y][x-1] == lt:
        nt += 1
    if x < len(cstate[0]) - 1 and cstate[y][x+1] == lt:
        nt += 1
    if y < len(cstate) - 1 and x > 0 and cstate[y+1][x-1] == lt:
        nt += 1
    if y < len(cstate) - 1 and cstate[y+1][x] == lt:
        nt += 1
    if y < len(cstate) - 1 and x < len(cstate[0]) - 1 and cstate[y+1][x+1] == lt:
        nt += 1
    return nt

def hashable(cstate):
    lumber = []
    trees = []
    for y, row in enumerate(cstate):
        for x, lt in enumerate(row):
            if lt == 1:
                trees.append((y,x))
            elif lt == 2:
                lumber.append((y,x))
    return tuple(lumber + [(-1,-1)] + trees)

seen = dict()
t = 0
while True:
    hs = hashable(cstate)
    if hs in seen:
        break
    seen[hs] = t
    nstate = [[0 for _ in cstate[0]] for _ in cstate]
    for (y, row) in enumerate(cstate):
        for (x, cell) in enumerate(row):
            if cell == 0:
                if ntype(1, y, x, cstate) >= 3:
                    nstate[y][x] = 1
            elif cell == 1:
                if ntype(2, y, x, cstate) >= 3:
                    nstate[y][x] = 2
                else:
                    nstate[y][x] = 1
            else:
                if ntype(2, y, x, cstate) and ntype(1, y, x, cstate):
                    nstate[y][x] = 2
                else:
                    nstate[y][x] = 0

    cstate = nstate
    t += 1

#found a cycle
cyclelength = t - seen[hs]
cycleoffset = seen[hs]
#closest time to a billion that my cycle state will be seen
ncycles = (1000000000 - cycleoffset)//cyclelength
lastcycletime = cycleoffset + ncycles * cyclelength
#finish off the last few steps
for _ in range(1000000000 - lastcycletime):
    nstate = [[0 for _ in cstate[0]] for _ in cstate]
    for (y, row) in enumerate(cstate):
        for (x, cell) in enumerate(row):
            if cell == 0:
                if ntype(1, y, x, cstate) >= 3:
                    nstate[y][x] = 1
            elif cell == 1:
                if ntype(2, y, x, cstate) >= 3:
                    nstate[y][x] = 2
                else:
                    nstate[y][x] = 1
            else:
                if ntype(2, y, x, cstate) and ntype(1, y, x, cstate):
                    nstate[y][x] = 2
                else:
                    nstate[y][x] = 0

    cstate = nstate

nlum = sum([sum([x == 2 for x in row]) for row in cstate])
ntree = sum([sum([x == 1 for x in row]) for row in cstate])
print(nlum * ntree)