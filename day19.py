with open("input19.txt") as f:
    prog = f.readlines()

ipreg = int(prog[0].split()[1])

instrs = [code.split() for code in prog[1:]]
tcodes = []
for instr in instrs:
    tcode = []
    i = instr[0]
    if i == "addr":
        tcode.append(0)
    elif i == "addi":
        tcode.append(1)
    elif i == "mulr":
        tcode.append(2)
    elif i == "muli":
        tcode.append(3)
    elif i == "banr":
        tcode.append(4)
    elif i == "bani":
        tcode.append(5)
    elif i == "borr":
        tcode.append(6)
    elif i == "bori":
        tcode.append(7)
    elif i == "setr":
        tcode.append(8)
    elif i == "seti":
        tcode.append(9)
    elif i == "gtir":
        tcode.append(10)
    elif i == "gtri":
        tcode.append(11)
    elif i == "gtrr":
        tcode.append(12)
    elif i == "eqir":
        tcode.append(13)
    elif i == "eqri":
        tcode.append(14)
    elif i == "eqrr":
        tcode.append(15)
    args = list(map(int,instr[1:]))
    tcode.extend(args)
    tcodes.append(tcode)

# part 1
reg = [0,0,0,0,0,0]
while reg[ipreg] < len(tcodes):
    tcode = tcodes[reg[ipreg]]
    i = tcode[0]
    if i == 0:
        reg[tcode[3]] = reg[tcode[1]] + reg[tcode[2]]
    elif i == 1:
        reg[tcode[3]] = reg[tcode[1]] + tcode[2]
    elif i == 2:
        reg[tcode[3]] = reg[tcode[1]] * reg[tcode[2]]
    elif i == 3:
        reg[tcode[3]] = reg[tcode[1]] * tcode[2]
    elif i == 4:
        reg[tcode[3]] = reg[tcode[1]] & reg[tcode[2]]
    elif i == 5:
        reg[tcode[3]] = reg[tcode[1]] & tcode[2]
    elif i == 6:
        reg[tcode[3]] = reg[tcode[1]] | reg[tcode[2]]
    elif i == 7:
        reg[tcode[3]] = reg[tcode[1]] | tcode[2]
    elif i == 8:
        reg[tcode[3]] = reg[tcode[1]]
    elif i == 9:
        reg[tcode[3]] = tcode[1]
    elif i == 10:
        reg[tcode[3]] = int(tcode[1] > reg[tcode[2]])
    elif i == 11:
        reg[tcode[3]] = int(reg[tcode[1]] > tcode[2])
    elif i == 12:
        reg[tcode[3]] = int(reg[tcode[1]] > reg[tcode[2]])
    elif i == 13:
        reg[tcode[3]] = int(tcode[1] == reg[tcode[2]])
    elif i == 14:
        reg[tcode[3]] = int(reg[tcode[1]] == tcode[2])
    elif i == 15:
        reg[tcode[3]] = int(reg[tcode[1]] == reg[tcode[2]])

    reg[ipreg] += 1

print(reg[0])

#part 2
reg = [1,0,0,0,0,0]
#just need to run the program till we know what the (constant) value of r5 is
for _ in range(50):
    tcode = tcodes[reg[ipreg]]
    i = tcode[0]
    if i == 0:
        reg[tcode[3]] = reg[tcode[1]] + reg[tcode[2]]
    elif i == 1:
        reg[tcode[3]] = reg[tcode[1]] + tcode[2]
    elif i == 2:
        reg[tcode[3]] = reg[tcode[1]] * reg[tcode[2]]
    elif i == 3:
        reg[tcode[3]] = reg[tcode[1]] * tcode[2]
    elif i == 4:
        reg[tcode[3]] = reg[tcode[1]] & reg[tcode[2]]
    elif i == 5:
        reg[tcode[3]] = reg[tcode[1]] & tcode[2]
    elif i == 6:
        reg[tcode[3]] = reg[tcode[1]] | reg[tcode[2]]
    elif i == 7:
        reg[tcode[3]] = reg[tcode[1]] | tcode[2]
    elif i == 8:
        reg[tcode[3]] = reg[tcode[1]]
    elif i == 9:
        reg[tcode[3]] = tcode[1]
    elif i == 10:
        reg[tcode[3]] = int(tcode[1] > reg[tcode[2]])
    elif i == 11:
        reg[tcode[3]] = int(reg[tcode[1]] > tcode[2])
    elif i == 12:
        reg[tcode[3]] = int(reg[tcode[1]] > reg[tcode[2]])
    elif i == 13:
        reg[tcode[3]] = int(tcode[1] == reg[tcode[2]])
    elif i == 14:
        reg[tcode[3]] = int(reg[tcode[1]] == tcode[2])
    elif i == 15:
        reg[tcode[3]] = int(reg[tcode[1]] == reg[tcode[2]])

    reg[ipreg] += 1

r5 = reg[5]
print(r5)
x = 0
for div in range(1,r5+1):
    if r5 % div == 0:
        x += div
print(x)