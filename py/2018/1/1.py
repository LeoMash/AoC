f = '1.in'
D = open(f).read().strip()
R = [int(line) for line in D.splitlines()]

ans1 = sum(R)
print(ans1)

ans2 = 0
vis = set()
i = 0
while True:
    r = R[i % len(R)]
    ans2 += r
    if ans2 in vis:
        break
    vis.add(ans2)
    i += 1
print(ans2)