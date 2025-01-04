from collections import defaultdict

f = '5.in'
D = open(f).read().strip()
CMD = [int(x) for x in D.split()]
print(CMD)

part2 = True
pos = 0
ans1 = 0
while 0 <= pos < len(CMD):
    jmp = CMD[pos]
    if jmp < 3 or not part2:
        d = 1
    else:
        d = -1
    CMD[pos] += d
    pos = pos + jmp
    ans1 += 1
print(ans1)
