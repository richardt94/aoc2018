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

print(maxlen(1))
