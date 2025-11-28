import re

# f = '3_test.in'
f = '3.in'
D = open(f).read().strip()
L = D.splitlines()

N = 1001
F = [[set() for i in range(N)] for j in range(N)]

R = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")

P = []

for l in range(len(L)):
    line = L[l]
    m = R.match(line)
    assert m
    idx = int(m.group(1))
    x = int(m.group(2))
    y = int(m.group(3))
    w = int(m.group(4))
    h = int(m.group(5))
    P.append((idx, x, y, w, h))

for idx, x, y, w, h in P:
    for i in range(w):
        for j in range(h):
            F[x + i][y + j].add(idx)

# print(F)

ans1 = 0
for i in range(N):
    for j in range(N):
        if len(F[i][j]) > 1:
            ans1 += 1
print(ans1)

ans2 = 0
for idx, x, y, w, h in P:
    sq = 0
    for i in range(w):
        for j in range(h):
             sq += len(F[x + i][y + j])
    if sq == w * h:
        ans2 = idx
        break
print(ans2)
