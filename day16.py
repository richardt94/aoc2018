import re

def testop(i, tcode, br, ar):
    if i == 0 and ar[tcode[3]] == br[tcode[1]] + br[tcode[2]]:
        return True
    if i == 1 and ar[tcode[3]] == br[tcode[1]] + tcode[2]:
        return True
    if i == 2 and ar[tcode[3]] == br[tcode[1]] * br[tcode[2]]:
        return True
    if i == 3 and ar[tcode[3]] == br[tcode[1]] * tcode[2]:
        return True
    if i == 4 and ar[tcode[3]] == br[tcode[1]] & br[tcode[2]]:
        return True
    if i == 5 and ar[tcode[3]] == br[tcode[1]] & tcode[2]:
        return True
    if i == 6 and ar[tcode[3]] == br[tcode[1]] | br[tcode[2]]:
        return True
    if i == 7 and ar[tcode[3]] == br[tcode[1]] | tcode[2]:
        return True
    if i == 8 and ar[tcode[3]] == br[tcode[1]]:
        return True
    if i == 9 and ar[tcode[3]] == tcode[1]:
        return True
    if i == 10 and ar[tcode[3]] == (tcode[1] > br[tcode[2]]):
        return True
    if i == 11 and ar[tcode[3]] == (br[tcode[1]] > tcode[2]):
        return True
    if i == 12 and ar[tcode[3]] == (br[tcode[1]] > br[tcode[2]]):
        return True
    if i == 13 and ar[tcode[3]] == (tcode[1] == br[tcode[2]]):
        return True
    if i == 14 and ar[tcode[3]] == (br[tcode[1]] == tcode[2]):
        return True
    if i == 15 and ar[tcode[3]] == (br[tcode[1]] == br[tcode[2]]):
        return True
    return False

with open("input16.txt") as f:
    pstr = f.read()

samples = pstr.split("\n\n")

samplergx = re.compile(r"Before: \[([0-9, ]+)\]\n([0-9 ]+)\nAfter:  \[([0-9, ]+)\]")

possible = [[True for _ in range(16)] for _ in range(16)]
for sample in samples:
    m = samplergx.match(sample)
    if not m:
        continue
    br = list(map(int, m.group(1).split(", ")))
    tcode = list(map(int, m.group(2).split()))
    ar = list(map(int, m.group(3).split(", ")))
    opcode = tcode[0]
    for i in range(16):
        if possible[opcode][i]:
            possible[opcode][i] = testop(i, tcode, br, ar)

assigned = 0
opmap = [0 for _ in range(16)]
while assigned < 16:
    for i, p in enumerate(possible):
        if sum(p) == 1:
            for j, isp in enumerate(p):
                if isp:
                    assigned += 1
                    opmap[i] = j
                    for others in possible:
                        others[j] = False
                    break

program = pstr.split("\n\n\n\n")[1].strip().split("\n")
program = [list(map(int, instruction.split())) for instruction in program]

reg = [0,0,0,0]
for tcode in program:
    i = opmap[tcode[0]]
    if i == 0:
        reg[tcode[3]] = reg[tcode[1]] + reg[tcode[2]]
    if i == 1:
        reg[tcode[3]] = reg[tcode[1]] + tcode[2]
    if i == 2:
        reg[tcode[3]] = reg[tcode[1]] * reg[tcode[2]]
    if i == 3:
        reg[tcode[3]] = reg[tcode[1]] * tcode[2]
    if i == 4:
        reg[tcode[3]] = reg[tcode[1]] & reg[tcode[2]]
    if i == 5:
        reg[tcode[3]] = reg[tcode[1]] & tcode[2]
    if i == 6:
        reg[tcode[3]] = reg[tcode[1]] | reg[tcode[2]]
    if i == 7:
        reg[tcode[3]] = reg[tcode[1]] | tcode[2]
    if i == 8:
        reg[tcode[3]] = reg[tcode[1]]
    if i == 9:
        reg[tcode[3]] = tcode[1]
    if i == 10:
        reg[tcode[3]] = int(tcode[1] > reg[tcode[2]])
    if i == 11:
        reg[tcode[3]] = int(reg[tcode[1]] > tcode[2])
    if i == 12:
        reg[tcode[3]] = int(reg[tcode[1]] > reg[tcode[2]])
    if i == 13:
        reg[tcode[3]] = int(tcode[1] == reg[tcode[2]])
    if i == 14:
        reg[tcode[3]] = int(reg[tcode[1]] == tcode[2])
    if i == 15:
        reg[tcode[3]] = int(reg[tcode[1]] == reg[tcode[2]])
print(reg[0])