from collections import defaultdict

f = '3.in'
D = open(f).read().strip()
N = int(D)

x = y  = 0
dx = 0
dy = -1
step = 1

while step != N:
    if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
        dx, dy = -dy, dx
    x, y = x + dx, y + dy
    step += 1
ans1 = abs(x) + abs(y)
print(ans1)

MAT3 = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1]]
x = y = 0
dx = 0
dy = -1
grid = defaultdict(int)
grid[(x, y)] = 1
while True:
    total = sum(grid[(x + dx, y + dy)] for dx, dy in MAT3)
    if total > N:
        ans2 = total
        break
    grid[(x, y)] = total
    if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
        dx, dy = -dy, dx
    x, y = x + dx, y + dy
print(ans2)


