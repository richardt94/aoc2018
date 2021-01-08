twos = 0
threes = 0
with open("input2.txt") as f:
    boxes = [box.rstrip() for box in f.readlines()]

for box in boxes:
    counts = [0 for _ in range(26)]
    for ch in box:
        counts[ord(ch) - ord('a')] += 1
    is2, is3 = False, False
    for c in counts:
        if c == 2:
            is2 = True
        if c == 3:
            is3 = True
    if is2:
        twos += 1
    if is3:
        threes += 1

print(twos * threes)

for box in boxes:
    for i in range(len(box)):
        nbox = list(box)
        for nch in range(26):
            if nch == ord(box[i]) - ord('a'):
                continue
            nbox[i] = chr(ord('a') + nch)
            if "".join(nbox) in boxes:
                print("".join(nbox[:i] + nbox[(i+1):]))