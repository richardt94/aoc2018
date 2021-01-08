freq = 0

with open('input1.txt','r') as f:
   deltas = f.readlines()

deltas = [int(delta) for delta in deltas]

freqs = []

for delta in deltas:
   freq += delta
   freqs.append(freq)

done = False

cfreq = freqs[-1]
print(cfreq) #pt1
visited = set(freqs)

while not done:
   for delta in deltas:
      cfreq += delta
      if cfreq in visited:
         done = True
         break
      visited.add(cfreq)
print(cfreq) #pt2
