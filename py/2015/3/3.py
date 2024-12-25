f = '3.in'
D = open(f).read().strip()

DIRS = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
}

sx, sy = 0, 0
VIS = {(sx, sy)}
for c in D:
    dx, dy = DIRS[c]
    sx, sy = sx + dx, sy + dy
    VIS.add((sx, sy))

print(len(VIS))

sx, sy = 0, 0
sx2, sy2 = 0, 0
VIS = {(sx, sy)}
for i, c in enumerate(D):
    dx, dy = DIRS[c]
    if i % 2:
        sx += dx
        sy += dy
        VIS.add((sx, sy))
    else:
        sx2 += dx
        sy2 += dy
        VIS.add((sx2, sy2))

print(len(VIS))
