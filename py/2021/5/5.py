from collections import defaultdict

f = '5.in'
D = open(f).read().strip()
lines = [line for line in D.splitlines() if line]

M = defaultdict(int)
M2 = defaultdict(int)
for line in lines:
    fr, to = line.split('->')
    fr = list(map(int, fr.strip().split(',')))
    to = list(map(int, to.strip().split(',')))
    print(fr, to)
    if fr[0] == to[0]:
        x = fr[0]
        y1 = min(fr[1], to[1])
        y2 = max(fr[1], to[1])
        for y in range(y1, y2 + 1):
            M[(x, y)] += 1
            M2[(x, y)] += 1
    elif fr[1] == to[1]:
        y = fr[1]
        x1 = min(fr[0], to[0])
        x2 = max(fr[0], to[0])
        for x in range(x1, x2 + 1):
            M[(x, y)] += 1
            M2[(x, y)] += 1
    elif abs(fr[0] - to[0]) == abs(fr[1] - to[1]):
        x_step = 1 if to[0] > fr[0] else -1
        y_step = 1 if to[1] > fr[1] else -1
        x, y = fr[0], fr[1]
        while x != to[0] + x_step and y != to[1] + y_step:
            M2[(x, y)] += 1
            x += x_step
            y += y_step

ans1 = 0
for k, v in M.items():
    if v > 1:
        ans1 += 1
print(ans1)
ans2 = 0
for k, v in M2.items():
    if v > 1:
        ans2 += 1
print(ans2)
