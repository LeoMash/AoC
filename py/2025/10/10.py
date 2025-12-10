import re

f = '10.in'
# f = '10_test.in'
D = open(f).read().strip().splitlines()
L = []

RE = re.compile('^\[(.*)\] (\(.*\))+ {(.*)}$')
for line in D:
    m = RE.match(line)
    assert m is not None
    l = m.group(1)
    t = m.group(2)
    t = t.replace('(', '')
    t = t.replace(')', '')
    t = t.split()
    t = [list(map(int, x.split(','))) for x in t]
    j = list(map(int, m.group(3).split(',')))
    L.append((l,j,t))

import sys
sys.setrecursionlimit(200000)

ans1 = 0
for l in L:
    print(l)
    V = tuple([0] * len(l[0]))
    VT = tuple([0 if x == '.' else 1 for x in l[0]])
    print(VT)

    DIST = {}
    def go(v, dist):
        if v in DIST:
            d = DIST[v]
            if d <= dist:
                return
        DIST[v] = dist
        if v == VT:
            return
        toggles = l[2]
        for toggle in toggles:
            Vn = list(v)
            for tt in toggle:
                Vn[tt] = 0 if Vn[tt] else 1
            vn = tuple(Vn)
            go(vn, dist + 1)

    go(V, 0)
    mindist = DIST[VT]
    print(mindist)
print(ans1)

# ans2 = 0
# for l in L:
#     print(l)
#     V = tuple([0] * len(l[0]))
#     JT = tuple(l[1])
#     DIST = {}
#     N = len(JT)
#
#     def go2(v, dist):
#         if v in DIST:
#             d = DIST[v]
#             if d <= dist:
#                 return
#         DIST[v] = dist
#         for i in range(N):
#             j = v[i]
#             jt = JT[i]
#             if j > jt:
#                 return
#         if v == JT:
#             return
#         toggles = l[2]
#         for toggle in toggles:
#             Vn = list(v)
#             for tt in toggle:
#                 Vn[tt] += 1
#             vn = tuple(Vn)
#             go2(vn, dist + 1)
#
#
#     go2(V, 0)
#     mindist = DIST[JT]
#     print(mindist)
#     ans2 += mindist
# print(ans2)

import z3

ans2 = 0
for l in L:
    J = l[1]
    T = l[2]
    N = len(T)
    vars = [z3.Int(f"t_{i}") for i in range(N)]
    solver = z3.Optimize()
    for ji, jval in enumerate(J):
        f = sum(vars[i] for i, t in enumerate(T) if ji in t)
        solver.add(z3.And(f == jval))

    solver.add(z3.And([v >= 0 for v in vars])) # can't press toggles negative amount
    solver.minimize(sum(vars))
    assert solver.check() == z3.sat

    m = solver.model()
    s = 0
    for v in vars:
        s += m[v].as_long()
    print(s)
    ans2 += s
print(ans2)