from collections import namedtuple
import heapq
import re

Cube = namedtuple('Cube', 'x0 x1 y0 y1 z0 z1')

#manhattan distance between point and closest point in cube
def distTo(x, y, z, cube):
    x0, x1, y0, y1, z0, z1 = cube.x0, cube.x1, cube.y0, cube.y1, cube.z0, cube.z1
    dx = min(abs(x-x0), abs(x-x1)) if (x-x0) * (x-x1) > 0 else 0
    dy = min(abs(y-y0), abs(y-y1)) if (y-y0) * (y-y1) > 0 else 0
    dz = min(abs(z-z0), abs(z-z1)) if (z-z0) * (z-z1) > 0 else 0
    return dx + dy + dz

pointrgx = re.compile(r"pos=<([\-0-9]+),([\-0-9]+),([\-0-9]+)>, r=([0-9]+)")
points = []
with open("input23.txt") as f:
    for line in f:
        m = pointrgx.match(line)
        if not m:
            continue
        points.append(tuple(int(m.group(i)) for i in range(1,5)))
xp, yp, zp = lambda p: p[0], lambda p: p[1], lambda p: p[2]
x0, x1 = min(points, key = xp)[0], max(points, key = xp)[0]
y0, y1 = min(points, key = yp)[1], max(points, key = yp)[1]
z0, z1 = min(points, key = zp)[2], max(points, key = zp)[2]

def ninr(cube):
    n = 0
    for p in points:
        n += 1 if distTo(p[0], p[1], p[2], cube) <= p[3] else 0
    return n

#need a priority queue where "priority" is
#1. number of points in range
#2. distance from origin
cu = Cube(x0,x1,y0,y1,z0,z1)
d = distTo(0, 0, 0, cu)
pr = 0
npt = len(points)
best = npt
bestd = max(abs(x0), abs(x1)) + max(abs(y0), abs(y1)) + max(abs(z0), abs(z1))
bestpt = (0,0,0)
q = [(pr,d,cu)]
visited = set()
while q:
    pr, _, cu = heapq.heappop(q)
    if pr > best:
        #no cubes left in the queue will allow us to equal our best score so far
        break
    if cu in visited:
        continue
    visited.add(cu)
    #consider eight equal divisions of the cube
    midx, midy, midz = (cu.x0 + cu.x1)//2, (cu.y0 + cu.y1)//2, (cu.z0 + cu.z1)//2
    for xhalf in range(2):
        for yhalf in range(2):
            for zhalf in range(2):
                x0, x1 = cu.x0 * (1 - xhalf) + (midx + 1) * xhalf, midx * (1 - xhalf) + cu.x1 * xhalf
                y0, y1 = cu.y0 * (1 - yhalf) + (midy + 1) * yhalf, midy * (1 - yhalf) + cu.y1 * yhalf
                z0, z1 = cu.z0 * (1 - zhalf) + (midz + 1) * zhalf, midz * (1 - zhalf) + cu.z1 * zhalf
                if z0 > z1 or y0 > y1 or x0 > x1:
                    #this region has no points in it so ignore it
                    continue
                elif z0 == z1 and y0 == y1 and x0 == x1:
                    #this is a single point
                    p = Cube(x0,x1,y0,y1,z0,z1)
                    pointpr = npt - ninr(p)
                    pointd = distTo(0,0,0,p)
                    if pointpr < best:
                        best = pointpr
                        bestd = pointd
                        bestpt = (x0,y0,z0)
                    elif pointpr == best and pointd < bestd:
                        bestd = pointd
                        bestpt = (x0,y0,z0)
                else:
                    #push on the queue
                    nextcu = Cube(x0,x1,y0,y1,z0,z1)
                    if nextcu not in visited:
                        nextpr = npt - ninr(nextcu)
                        nextd = distTo(0,0,0,nextcu)
                        heapq.heappush(q,(nextpr, nextd, nextcu))

print(npt - best, bestd, bestpt)

