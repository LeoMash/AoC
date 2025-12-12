from collections import deque

f = '12.in'
# f = '12_test.in'
F = open(f).read().strip()
F = F.split('\n\n')
P = []
for p in F[:-1]:
    pp = p.splitlines()[1:]
    P.append(pp)
print(P)

PSZ = []
for p in P:
    psz = 0
    for i in range(3):
        for j in range(3):
            if pp[i][j] == '#':
                psz += 1
    PSZ.append(psz)
print(PSZ)

S = []
for line in F[-1].splitlines():
    u, v = line.split(':')
    u = list(map(int, u.strip().split('x')))
    v = list(map(int, v.strip().split()))
    S.append((u,v))
print(S)

# fast check
ans1 = 0
for s in S:
    x,y = s[0]
    pp = s[1]
    totalsz = 0
    for i, npi in enumerate(pp):
        totalsz += PSZ[i] * npi
    if totalsz > x * y:
        print(x, y, f"({x * y}): ", totalsz, "BAD")
    else:
        full_x = x // 3
        full_y = y // 3
        squares = full_x * full_y
        parts = sum(pp)
        if parts <= squares:
            print(x, y, f"({x * y}): ", totalsz, "GOOD", f"{parts} <= {squares}")
            ans1 += 1
        else:
            print(x, y, f"({x * y}): ", totalsz, "HARD", f"{parts} > {squares}")
            assert False
print(ans1)