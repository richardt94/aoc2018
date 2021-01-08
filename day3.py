import re
claimrgx = re.compile("#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)")

with open("input3.txt") as f:
    claims = f.readlines()

claimed = dict()

overlap = 0
for claim in claims:
    m = claimrgx.match(claim)
    if not m:
        continue
    x0, y0, sx, sy = (int(m.group(i)) for i in range(2,6))
    for x in range(x0, x0+sx):
        for y in range(y0, y0+sy):
            if (x,y) in claimed:
                if claimed[(x,y)] == 1:
                    overlap += 1
                claimed[(x,y)] += 1
            else:
                claimed[(x,y)] = 1

print(overlap)

#part 2
for claim in claims:
    m = claimrgx.match(claim)
    if not m:
        continue
    cid, x0, y0, sx, sy = (int(m.group(i)) for i in range(1,6))
    
    nooverlap = True
    for x in range(x0, x0+sx):
        for y in range(y0, y0+sy):
            if claimed[(x,y)] != 1:
                nooverlap = False
    if nooverlap:
        print(cid)