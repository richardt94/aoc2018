pwr = lambda x, y, sn: (((x+10)*y+sn)*(x+10)//100 % 10) - 5

#partial sums
ps = [[0 for _ in range(300)] for _ in range(300)]
mp = 0
x = 0
y = 0
s = 0
for i in range(300):
    for j in range(300):
        ps[i][j] = pwr(i + 1, j + 1, 2568)
        if i > 0:
            ps[i][j] += ps[i-1][j]
        if j > 0:
            ps[i][j] += ps[i][j-1]
        if i > 0 and j > 0:
            ps[i][j] -= ps[i-1][j-1]

        for sz in range(1,min(i,j) + 1):
            p = ps[i][j]
            if i - sz >= 0:
                p -= ps[i-sz][j] 
            if j - sz >= 0:
                p -= ps[i][j-sz]
            if i - sz >= 0 and j - sz >= 0:
                p += ps[i-sz][j-sz]
            if p > mp:
                mp = p
                x = i - sz + 2
                y = j - sz + 2
                s = sz

print(x,y,s)

print(mp)