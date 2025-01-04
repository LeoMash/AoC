f = '2.in'
# f = '2_test.in'
D = open(f).read().strip()
CMD = [x.strip() for x in D.splitlines()]

print(CMD)

DIR4 = (
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
)
DIR_MAP = {
    "U": 0,
    "R": 1,
    "D": 2,
    "L": 3,
}

PAD = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

PAD2 = [
    [None, None, '1', None, None],
    [None,  '2', '3',  '4', None],
    [ '5',  '6', '7',  '8',  '9'],
    [None,  'A', 'B',  'C', None],
    [None, None, 'D', None, None],
]

x, y = 1, 1
res = ''
for cmd in CMD:
    for c in cmd:
        d = DIR_MAP[c]
        dx, dy = DIR4[d]
        if 0 <= x + dx <= 2:
            x += dx
        if 0 <= y + dy <= 2:
            y += dy
    res += str(PAD[y][x])
print(res)

x, y = 0, 2
res = ''
for cmd in CMD:
    for c in cmd:
        d = DIR_MAP[c]
        dx, dy = DIR4[d]
        if 0 <= x + dx <= 4 and 0 <= y + dy <= 4 and PAD2[y + dy][x + dx]:
            x += dx
            y += dy
    res += PAD2[y][x]
print(res)