import re
from collections import deque
irgx = re.compile("([0-9]+) players; last marble is worth ([0-9]+) points")
with open("input9.txt") as f:
    m = irgx.match(f.read())

np, lmar = int(m.group(1)), int(m.group(2))

def playmarbles(np, lmar):
    circle = deque([0])
    score = [0 for _ in range(np)]

    for mar in range(1,lmar + 1):
        if not mar % 23:
            score[(mar - 1)%np] += mar
            circle.rotate(7)
            score[(mar - 1)%np] += circle.popleft()
            continue
        circle.rotate(-2)
        circle.appendleft(mar)

    return max(score)

print(playmarbles(np,lmar))
print(playmarbles(np,100*lmar))