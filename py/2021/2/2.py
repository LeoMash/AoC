f = '2.in'
D = open(f).read().strip()
R = [line.split() for line in D.splitlines()]
# print(R)

hor1 =  0
depth1 = 0
hor2 =  0
depth2 = 0
aim = 0
for d, x in R:
    x = int(x)
    if d[0] == 'f':
        hor1 += x
        hor2 += x
        depth2 += aim * x
    elif d[0] == 'u':
        depth1 -= x
        aim -= x
    else:
        depth1 += x
        aim += x
print(hor1 * depth1)
print(hor2 * depth2)

