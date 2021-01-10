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
done = False
time = 0
nworkers = 5
busy = [-1 for _ in range(nworkers)]
curl = [-1 for _ in range(nworkers)]
while not done:
    #clean up done workers
    for w in range(nworkers):
        if busy[w] == 0:
            order += chr(curl[w] + 65)
            for child in children[curl[w]]:
                prereq[child].remove(curl[w])
                if len(prereq[child]) == 0:
                    heapq.heappush(pq,child)
    #pop queue onto free workers
    for w in range(nworkers):
        if busy[w] <= 0 and len(pq) > 0:
            curl[w] = heapq.heappop(pq)
            busy[w] = curl[w] + 61
    #set the done flag if no worker is working on anything
    done = True
    for w in range(nworkers):
        if busy[w] > 0:
            done = False
        busy[w] -= 1
    time += 1
    
print(order)
print(time - 1)