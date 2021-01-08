import re
claimrgx = re.compile("#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)")

with open("input3.txt") as f:
    claims = f.readlines()

claimed = set()

for claim in claims:
    m = claimrgx.match(claim)
    if not m:
        continue
    