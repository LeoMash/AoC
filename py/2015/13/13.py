import re
from collections import defaultdict
from functools import cache

f = '13.in'
# f = '13_test.in'
D = open(f).read().strip()

R = re.compile("(.*) would (gain|lose) (.*) happiness units by sitting next to (.*).")

G = defaultdict(dict)
for line in D.splitlines():
    m = R.match(line)
    assert m is not None
    a = m.group(1)
    sign = -1 if m.group(2) == 'lose' else 1
    val = sign * int(m.group(3))
    b = m.group(4)
    G[a][b] = val

# G = dict(G)
print(G)

def get_sum(ulist):
    s = 0
    for i, v in enumerate(ulist):
        u = ulist[i - 1]
        w = ulist[(i + 1) % len(ulist)]
        s += G[v][u]
        s += G[v][w]
    return s


def go(ulist):
    if len(ulist) == len(G):
        return get_sum(ulist)
    maxsum = -float('inf')
    for v in G:
        if v in ulist:
            continue
        ulist.append(v)
        maxsum = max(maxsum, go(ulist))
        ulist.pop()
    return maxsum

ans1 = go([])
print(ans1)

g = list(G.keys())
for v in g:
    G[v]['me'] = 0
    G['me'][v] = 0
ans2 = go([])
print(ans2)