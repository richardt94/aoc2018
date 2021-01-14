with open("input13.txt") as f:
    track = [list(l.rstrip("\n")) for l in f.readlines()]


carts = dict()
for y, l in enumerate(track):
    newl = ""
    for x, ch in enumerate(l):
        if ch == '>':
            newl += '-'
            carts[(x,y)] = (1,0,0)
        elif ch == '<':
            newl += '-'
            carts[(x,y)] = (-1,0,0)
        elif ch == '^':
            newl += '|'
            carts[(x,y)] = (0,-1,0)
        elif ch == 'v':
            newl += '|'
            carts[(x,y)] = (0,1,0)

for _ in range(17710):
    nxtcarts = dict()
    crashed = []
    for c in carts:
        d = carts[c]
        nc = (c[0] + d[0], c[1] + d[1])
        if nc in nxtcarts:
            crashed.append(nc)
            continue
        #need to detect "half-step" crashes -
        #when this happens two carts will "swap"
        #so it should be easy to detect
        if c in nxtcarts and nc in carts:
            crashed.append(c)
            continue
        c = nc
        if track[c[1]][c[0]] == '/':
            d = (-d[1], -d[0], d[2])
        elif track[c[1]][c[0]] == '\\':
            d = (d[1], d[0], d[2])
        elif track[c[1]][c[0]] == '+':
            if d[2] == 0:
                if d[0]:
                    d = (0, -d[0], d[2])
                else:
                    d = (d[1], 0, d[2])
            elif d[2] == 2:
                if d[0]:
                    d = (0, d[0], d[2])
                else:
                    d = (-d[1], 0, d[2])
            d = (d[0], d[1], (d[2] + 1) % 3)
        nxtcarts[c] = d
    for c in crashed:
        del nxtcarts[c]
    carts = nxtcarts
print(carts)
