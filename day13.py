with open("input13.txt") as f:
    track = [list(l.rstrip("\n")) for l in f.readlines()]

carts = []
for y, l in enumerate(track):
    newl = ""
    for x, ch in enumerate(l):
        if ch == '>':
            newl += '-'
            carts.append((x,y,1,0,0))
        elif ch == '<':
            newl += '-'
            carts.append((x,y,-1,0,0))
        elif ch == '^':
            newl += '|'
            carts.append((x,y,0,-1,0))
        elif ch == 'v':
            newl += '|'
            carts.append((x,y,0,1,0))

while len(carts) > 1:
    carts.sort(key = lambda x: x[0])
    carts.sort(key = lambda x: x[1])
    nxtcarts = []
    crashed = [False for _ in carts]
    for i, c in enumerate(carts):
        nc = (c[0] + c[2], c[1] + c[3])
        for j, c2 in enumerate(nxtcarts):
            #ignore if something has already
            #crashed into and destroyed this cart
            if crashed[j]: continue
            if c2[0] == nc[0] and c2[1] == nc[1]:
                crashed[i] = True
                crashed[j] = True
        for j, c2 in enumerate(carts[i+1:]):
            if crashed[j+i+1]: continue
            if c2[0] == nc[0] and c2[1] == nc[1]:
                crashed[i] = True
                crashed[j+i+1] = True
        d = c[2:5]
        if track[nc[1]][nc[0]] == '/':
            d = (-c[3], -c[2], c[4])
        elif track[nc[1]][nc[0]] == '\\':
            d = (c[3], c[2], c[4])
        elif track[nc[1]][nc[0]] == '+':
            if c[4] == 0:
                if c[2]:
                    d = (0, -c[2], c[4])
                else:
                    d = (c[3], 0, c[4])
            elif c[4] == 2:
                if c[2]:
                    d = (0, c[2], c[4])
                else:
                    d = (-c[3], 0, c[4])
            d = (d[0], d[1], (d[2] + 1) % 3)
        nxtcarts.append((*nc,*d))
    #clean up
    carts = []
    for i, c in enumerate(nxtcarts):
        if not crashed[i]:
            carts.append(c)
print(carts)
