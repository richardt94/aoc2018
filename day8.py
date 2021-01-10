with open("input8.txt") as f:
    treespec = list(map(int, f.read().split()))

idx = 0
def readtree():
    global idx
    nch = treespec[idx]
    nmd = treespec[idx+1]
    idx += 2
    score = 0
    if nch > 0:
        scores = [0 for _ in range(nch)]
        for ch in range(nch):
            scores[ch] = readtree()
        for md in treespec[idx:idx+nmd]:
            if md > nch: continue
            score += scores[md-1]
    else: score = sum(treespec[idx:idx+nmd])
    idx += nmd
    return score

print(readtree())
