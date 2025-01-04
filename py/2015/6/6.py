import re

f = '6.in'
D = open(f).read().strip()

R = re.compile(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)')
A2I = {
    'turn on' : 0,
    'turn off' : 1,
    'toggle' : 2,
}
RULES = []
for line in D.splitlines():
    m = R.match(line)
    assert m
    t, a, b, c, d = m.groups()
    t, a, b, c, d = A2I[t], int(a), int(b), int(c), int(d)
    RULES.append((t, a, b, c, d))

N = 1000
# print(RULES)

def apply_rule(f, rule):
    t, a, b, c, d = rule
    for i in range(a, c + 1):
        for j in range(b, d + 1):
            if t == 0:
                f[i][j] = True
            elif t == 1:
                f[i][j] = False
            elif t == 2:
                f[i][j] = not f[i][j]

def apply_rule2(f, rule):
    t, a, b, c, d = rule
    for i in range(a, c + 1):
        for j in range(b, d + 1):
            if t == 0:
                f[i][j] += 1
            elif t == 1:
                if f[i][j] > 0:
                    f[i][j] -= 1
            elif t == 2:
                f[i][j] += 2

F = [[False for _ in range(N)] for _ in range(N)]
for r in RULES:
    apply_rule(F, r)
ans1 = 0
for i in range(N):
    for j in range(N):
        ans1 += F[i][j]
print(ans1)

F = [[0 for _ in range(N)] for _ in range(N)]
for r in RULES:
    apply_rule2(F, r)
ans2 = 0
for i in range(N):
    for j in range(N):
        ans2 += F[i][j]
print(ans2)
