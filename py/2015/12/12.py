import json
import re
from collections import defaultdict
from functools import cache

f = '12.in'
D = open(f).read().strip()

R = re.compile(r'-?\d+')

ans1 = 0
for d in re.findall(R, D):
    ans1 += int(d)
print(ans1)


def go(obj):
    sum = 0
    if isinstance(obj, dict):
        if 'red' not in obj.values():
            for k, v in obj.items():
                sum += go(v)
    elif isinstance(obj, list):
        for v in obj:
            sum += go(v)
    elif isinstance(obj, int):
        sum += obj
    else:
        assert isinstance(obj, str)
    return sum

j = json.loads(D)
ans2 = go(j)
print(ans2)