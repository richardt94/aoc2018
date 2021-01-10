import re
import heapq

srgx = re.compile("Step ([A-Z]) must be finished before step ([A-Z]) can begin.")
prereq = [set() for _ in range(26)]
children = [set() for _ in range(26)]
with open("input7.txt") as f:
    for line in f:
        m = srgx.match(line)
        fromi = ord(m.group(1))-65
        toi = ord(m.group(2))-65
        prereq[toi].add(fromi)
        children[fromi].add(toi)

pq = []
for i, (st,sf) in enumerate(zip(prereq,children)):
    if len(st) == 0 and len(sf) != 0:
        heapq.heappush(pq,i)

order = ""
while len(pq) > 0:
    curi = heapq.heappop(pq)
    order += chr(curi+65)
    for nexti in children[curi]:
        prereq[nexti].remove(curi)
        if len(prereq[nexti]) == 0:
            heapq.heappush(pq,nexti)
print(order)