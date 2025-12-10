import re

f = '10.in'
# f = '10_test.in'
D = open(f).read().strip().splitlines()
L = []

RE = re.compile(r'^\[(.*)] (\(.*\))+ {(.*)}$')
for line in D:
    m = RE.match(line)
    assert m is not None
    l = m.group(1)
    t = m.group(2)
    t = t.replace('(', '').replace(')', '').split()
    t = [list(map(int, x.split(','))) for x in t]
    j = list(map(int, m.group(3).split(',')))
    L.append((l,j,t))


import itertools

ans1 = 0
for l in L:
    print(l)
    V = 0
    VT = int(l[0].replace('#', '1').replace('.', '0')[::-1], 2)
    print(f"{VT:b}")
    T = l[2]
    T_MASKS = []
    for t in T:
        t_mask = 0
        for tt in t:
            t_mask |= (1 << tt)
        T_MASKS.append(t_mask)
    print([f"{m:b}" for m in T_MASKS])
    N = len(T)
    minsize = 0
    for t in range(1, N):
        for toggles in itertools.combinations(T_MASKS, t):
            mask = 0
            for m in toggles:
                mask ^= m
            if mask == VT:
                break
        else:
            continue
        minsize = t
        break
    else:
        assert False

    print(minsize)
    ans1 += minsize

print(ans1)

print("**********")

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