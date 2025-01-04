import re
from collections import defaultdict
from functools import cache

f = '9.in'
# f = '9_test.in'
D = open(f).read().strip()

R = re.compile("(.*) to (.*) = (.*)")

G = defaultdict(list)
for line in D.splitlines():
    m = R.match(line)
    assert m is not None
    a = m.group(1)
    b = m.group(2)
    c = int(m.group(3))
    G[a].append((b, c))
    G[b].append((a, c))

G = dict(G)
print(G)


def go(ulist, dist):
    if len(ulist) == len(G):
        return dist, dist
    u = ulist[-1]
    mindist = float('inf')
    maxdist = 0
    for v, d in G[u]:
        if v in ulist:
            continue
        ulist.append(v)
        a, b = go(ulist, dist + d)
        mindist = min(mindist, a)
        maxdist = max(maxdist, b)
        ulist.pop()
    return mindist, maxdist

ans1 = float('inf')
ans2 = 0
for u in G:
    a, b = go([u], 0)
    ans1 = min(ans1, a)
    ans2 = max(ans2, b)
print(ans1)
print(ans2)
