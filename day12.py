import re
def dothash2num(dh):
    num = 0
    for ch in dh:
        num *= 2
        if ch == "#":
            num += 1
    return num

with open("input12.txt") as f:
    spec = f.readlines()
initstate = spec[0].split()[-1]
offset = len(initstate) - 1
state = dothash2num(initstate)

rules = [0 for _ in range(32)]
transrgx = re.compile(r"([\.#]{5}) => #")
for rule in spec[2:]:
    m = transrgx.match(rule)
    if not m:
        continue
    rules[dothash2num(m.group(1))] = 1

t = 0
ooffset = 0
ostate = 0
while state != ostate:
    ostate = state
    ooffset = offset
    t += 1
    state <<= 4
    nstate = 0
    b = 0
    while state > 0:
        nstate += 2**b * rules[state%32]
        state >>= 1
        b += 1
    offset += 2
    while not nstate % 2:
        nstate >>= 1
        offset -= 1
    state = nstate
    # print("{:b}".format(state))

ntrans = 5 * 10**10 - (t-1)
transtep = offset - ooffset

#quick fast forward to 50b
offset = ooffset + ntrans*transtep

score = 0
b = offset
while state > 0:
    score += state % 2 * b
    state >>= 1
    b -= 1
print(score)
