import re

with open("input4.txt") as f:
    events = [e.rstrip() for e in f.readlines()]

timergx = re.compile(r"\[1518-(\d\d)-(\d\d) (\d\d):(\d\d)\]")
def timenumber(tstr):
    m = timergx.match(tstr)
    month = int(m.group(1))
    day = int(m.group(2))
    hour = int(m.group(3))
    minute = int(m.group(4))
    return 31*24*60*(month - 1) + 24*60*(day - 1) + 60*hour + minute

sortkeys = [timenumber(e) for e in events]
sortidxs = sorted(range(len(sortkeys)), key = lambda x: sortkeys[x])
sortedevents = [events[i] for i in sortidxs]

cguard = 0
minsasleep = [[0 for _ in range(60)] for _ in range(10000)]
smin = 0
for e in sortedevents:
    if e.endswith("begins shift"):
        cguard = int(e.split()[-3][1:])
    elif e.endswith("falls asleep"):
        m = timergx.match(e)
        smin = int(m.group(4))
    elif e.endswith("wakes up"):
        m = timergx.match(e)
        emin = int(m.group(4))
        for minute in range(smin, emin):
            minsasleep[cguard][minute] += 1

#part 1
tmins = [sum(mins) for mins in minsasleep]

sleepyguard = max(range(10000), key = lambda x: tmins[x])
print(sleepyguard)
sleepymin = max(range(60), key = lambda x: minsasleep[sleepyguard][x])
print(sleepymin)
print(sleepyguard*sleepymin)

#part 2
maxmins = [max(mins) for mins in minsasleep]

sleepyguard = max(range(10000), key = lambda x: maxmins[x])
print(sleepyguard)
sleepymin = max(range(60), key = lambda x: minsasleep[sleepyguard][x])
print(sleepymin)
print(sleepyguard*sleepymin)