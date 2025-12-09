from collections import defaultdict

f = '9.in'
# f = '9_test.in'
D = open(f).read().strip().splitlines()

C = []
for d in D:
    a, b = map(int, d.split(','))
    C.append((a, b))

CN = len(C)
print(CN)
print(C)

BY_X = defaultdict(list)
BY_Y = defaultdict(list)

for x, y in C:
    BY_X[x].append(y)
    BY_Y[y].append(x)
for ys in BY_X.values():
    assert len(ys) % 2 == 0
for xs in BY_Y.values():
    assert len(xs) % 2 == 0

H_SEGS = []
V_SEGS = []

for x, ys in BY_X.items():
    yss = sorted(ys)
    for i in range(0, len(yss), 2):
        a = [x, yss[i]]
        b = [x, yss[i + 1]]
        H_SEGS.append((a, b))
print(H_SEGS)
print(len(H_SEGS))

for y, xs in BY_Y.items():
    assert len(xs) % 2 == 0
    xss = sorted(xs)
    for i in range(0, len(xss), 2):
        a = [xss[i], y]
        b = [xss[i + 1], y]
        V_SEGS.append((a, b))
print(V_SEGS)
print(len(V_SEGS))

ans1 = 0
rect1 = 0, 0
ans2 = 0
rect2 = 0, 0
for i, a in enumerate(C):
    for j, b in enumerate(C[:i]):
        minx = min(a[0], b[0])
        maxx = max(a[0], b[0])

        miny = min(a[1], b[1])
        maxy = max(a[1], b[1])

        area = (maxx - minx + 1) * (maxy - miny + 1)
        # ans1 = max(ans1, area)
        if area > ans1:
            ans1 = area
            rect1 = i, j

        valid = True
        for h0, h1 in H_SEGS:
            hx = h0[0]
            hy0 = min(h0[1], h1[1])
            hy1 = max(h0[1], h1[1])
            if minx < hx < maxx and hy1 > miny and hy0 < maxy:
                break
        if not valid:
            continue

        for v0, v1 in V_SEGS:
            vy = v0[1]
            vx0 = min(v0[0], v1[0])
            vx1 = max(v0[0], v1[0])
            if miny < vy < maxy and vx1 > minx and vx0 < maxx:
                valid = False
                break
        if not valid:
            continue

        # ans2 = max(ans2, area)
        if area > ans2:
            ans2 = area
            rect2 = i, j

print(ans1)
print(rect1)
print(ans2)
print(rect2)
