f = '3.in'
D = open(f).read().strip()

R = []
for line in D.splitlines():
    sides = line.split()
    sides = [int(x) for x in sides]
    R.append(sides)

ans1 = 0
for r in R:
    rs = sorted(r)
    if rs[0] + rs[1] > rs[2]:
        ans1 += 1
print(ans1)

ans2 = 0
for i in range(0, len(R), 3):
    r1 = R[i]
    r2 = R[i + 1]
    r3 = R[i + 2]
    t1 = sorted([r1[0], r2[0], r3[0]])
    t2 = sorted([r1[1], r2[1], r3[1]])
    t3 = sorted([r1[2], r2[2], r3[2]])
    if t1[0] + t1[1] > t1[2]:
        ans2 += 1
    if t2[0] + t2[1] > t2[2]:
        ans2 += 1
    if t3[0] + t3[1] > t3[2]:
        ans2 += 1
print(ans2)