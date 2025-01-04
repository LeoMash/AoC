import re
from collections import defaultdict
from functools import cache

f = '10.in'
D = open(f).read().strip()
NUM = 40
NUM2 = 50

def encode(s):
    res = ''
    cur = 1
    curc = s[0]
    for c in s[1:]:
        if c == curc:
            cur += 1
        else:
            res += str(cur)
            res += curc
            cur = 1
            curc = c
    res += str(cur)
    res += curc
    return res

assert encode('1') == '11'
assert encode('11') == '21'
assert encode('21') == '1211'
assert encode('1211') == '111221'
assert encode('111221') == '312211'

s = D
for i in range(NUM):
    s = encode(s)
print(len(s))
for i in range(NUM2 - NUM):
    s = encode(s)
print(len(s))