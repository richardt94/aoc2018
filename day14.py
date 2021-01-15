e1 = 0
e2 = 1
pzi = [ord(c) - ord('0') for c in str(170641)]
rc = [3,7]
done = False
while not done:
    r1 = rc[e1]
    r2 = rc[e2]
    nr = r1 + r2
    if nr > 9:
        rc.append(1)
        if rc[-len(pzi):] == pzi:
            done = True
            continue
    rc.append(nr%10)
    e1 = (e1 + r1 + 1) % len(rc)
    e2 = (e2 + r2 + 1) % len(rc)
    if rc[-len(pzi):] == pzi:
        done = True
print(len(rc) - len(pzi))