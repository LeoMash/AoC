import re
from collections import defaultdict
from functools import cache

f = '15.in'
D = open(f).read().strip()

R = re.compile(r'-?\d')
G = []
for line in D.splitlines():
    m = R.findall(line)
    assert m is not None
    vals = []
    for val in m:
        vals.append(int(val))
    G.append(vals)
print(G)

