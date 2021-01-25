with open("input20.txt") as f:
    regexstr = f.read()

dirs = ['N', 'E', 'S', 'W']
def maxlen(sidx):
    mlens = []
    mlen = 0
    while True:
        if regexstr[sidx] in dirs:
            mlen += 1
        elif regexstr[sidx] == '(':
            mlg, sidx = maxlen(sidx+1)
            mlen += mlg
        elif regexstr[sidx] == '|':
            mlens.append(mlen)
            mlen = 0
        else:
            mlens.append(mlen)
            retval = 0 if 0 in mlens else max(mlens)
            return retval, sidx
        sidx += 1

print(maxlen(1)[0])

#the input doesn't contain non-trivial branches (i.e. two branching options which 'join' and
#are followed by the same sequence of movements), so every position in the string has a single
#(x,y) value associated. There will be some backtracking in 'detour' branches so we need to
#maintain a set of visited locations.

visited = set((0,0))
def ngt1000(x, y, distTo, sidx):
    nx = x
    ny = y
    nfar = 0
    ndt = distTo

    while True:
        if regexstr[sidx] in dirs:
            if regexstr[sidx] == 'W':
                nx -= 1
            elif regexstr[sidx] == 'E':
                nx += 1
            elif regexstr[sidx] == 'S':
                ny -= 1
            else:
                ny += 1
            ndt += 1
            if (nx, ny) not in visited:
                visited.add((nx,ny))
                if ndt >= 1000:
                    nfar += 1
        elif regexstr[sidx] == '|':
            nx = x 
            ny = y
            ndt = distTo
        elif regexstr[sidx] == '(':
            addnfar, sidx = ngt1000(nx, ny, ndt, sidx+1)
            nfar += addnfar
        else:
            return nfar, sidx
        sidx += 1

print(ngt1000(0,0,0,1)[0])




