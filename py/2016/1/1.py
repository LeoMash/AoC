f = '1.in'
D = open(f).read().strip()
CMD = [x.strip() for x in D.split(',')]

print(CMD)

DIR4 = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
)

ans1 = 0
x, y, d = 0, 0, 0

vis = set()
first = True
x2, y2 = None, None
for cmd in CMD:
    if cmd[0] == 'R':
        d = (d + 1) % 4
    else:
        d = (d + 3) % 4
    dx, dy = DIR4[d]
    dist = int(cmd[1:])
    for _ in range(dist):
        x, y = x + dx, y + dy
        if (x, y) in vis and first:
            x2, y2 = x, y
            first = False
        vis.add((x, y))

print(x, y)
print(abs(x) + abs(y))
print(x2, y2)
print(abs(x2) + abs(y2))