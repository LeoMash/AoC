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

V_SEGS = []
H_SEGS = []

for x, ys in BY_X.items():
    yss = sorted(ys)
    for i in range(0, len(yss), 2):
        a = [x, yss[i]]
        b = [x, yss[i + 1]]
        V_SEGS.append((a, b))
print(V_SEGS)
print(len(V_SEGS))

for y, xs in BY_Y.items():
    assert len(xs) % 2 == 0
    xss = sorted(xs)
    for i in range(0, len(xss), 2):
        a = [xss[i], y]
        b = [xss[i + 1], y]
        H_SEGS.append((a, b))
print(H_SEGS)
print(len(H_SEGS))

ans1 = 0
rect1 = 0, 0
ans2 = 0
rect2 = 0, 0
for i in range(CN - 1):
    a = C[i]
    for j in range(i + 1, CN):
        b = C[j]

        minx = min(a[0], b[0])
        maxx = max(a[0], b[0])

        miny = min(a[1], b[1])
        maxy = max(a[1], b[1])

        area = (maxx - minx + 1) * (maxy - miny + 1)
        # ans1 = max(ans1, area)
        if area > ans1:
            ans1 = area
            rect1 = i, j

        if (j - i == 2) or (i + CN - j) == 2:
            c = C[(i + 1) % CN]
            dx1 = c[0] - a[0]
            dx2 = b[0] - c[0]
            dy1 = c[1] - a[1]
            dy2 = b[1] - c[1]
            dot = dx1 * dy2 - dx2 * dy1
            if dot < 0:
                continue


        valid = True
        for v0, v1 in V_SEGS:
            vx = v0[0]
            vy0 = min(v0[1], v1[1])
            vy1 = max(v0[1], v1[1])
            if minx < vx < maxx and vy1 > miny and vy0 < maxy:
                valid = False
                break
        if not valid:
            continue

        for h0, h1 in H_SEGS:
            hy = h0[1]
            hx0 = min(h0[0], h1[0])
            hx1 = max(h0[0], h1[0])
            if miny < hy < maxy and hx1 > minx and hx0 < maxx:
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
