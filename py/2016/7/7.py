import itertools
import re

f = '7.in'
D = open(f).read().strip()

R = []
for line in D.splitlines():
    R.append(line.strip())

def abba(s):
    return any(a == d and b == c and a != b for a, b, c, d in zip(s, s[1:], s[2:], s[3:]))

def aba(s):
    for a, b, c in zip(s, s[1:], s[2:]):
        if a == c and a != b:
            yield b+a+b


def rule3(p1, p2):
    for x in p1:
        for bab in aba(x):
            for y in p2:
                if bab in y:
                    return True
    return False

ans1 = 0
ans2 = 0
for r in R:
    s = re.split(r'\[([^\]]+)\]', r)
    p1, p2 = s[::2], s[1::2]
    rule1 = any([abba(x) for x in p1])
    rule2 = not any([abba(x) for x in p2])
    ans1 += (rule1 and rule2)
    ans2 += rule3(p1, p2)

print(ans1)
print(ans2)
