f = '4.in'
D = open(f).read().strip()
lines = [line for line in D.splitlines() if line]
NUMS = list(map(int,lines[0].split(',')))
print(NUMS)

SZ = 5

BOARDS = []
for a,b,c,d,e in zip(lines[1::SZ], lines[2::SZ], lines[3::SZ], lines[4::SZ], lines[5::SZ]):
    BOARDS.append([a.split(),b.split(),c.split(),d.split(),e.split()])
NUM_BOARDS = len(BOARDS)

BOARDS_IDX = []
for board in BOARDS:
    board_idx = dict()
    for y in range(SZ):
        for x in range(SZ):
            board[y][x] = int(board[y][x])
            board_idx[board[y][x]] = (y, x)
    BOARDS_IDX.append(board_idx)
print(BOARDS)
print(BOARDS_IDX)


BOARDS_MARKS = []
for board in BOARDS:
    MARKS_H = [0 for _ in range(5)]
    MARKS_V = [0 for _ in range(5)]
    BOARDS_MARKS.append((MARKS_H, MARKS_V))
print(BOARDS_MARKS)


def calc_score(board, h, win_num):
    sum = 0
    for y in range(SZ):
        inv_mask_x = ~h[y]
        for x in range(SZ):
            if inv_mask_x & (1 << x):
                sum += board[y][x]
    return sum * win_num

WON_BOARDS = [False for _ in range(NUM_BOARDS)]
for num in NUMS:
    print(num)
    for i in range(NUM_BOARDS):
        if WON_BOARDS[i]:
            continue
        idx = BOARDS_IDX[i]
        y, x = idx.get(num, (-1,-1))
        if y == -1:
            continue
        h, v = BOARDS_MARKS[i]
        mask_y = 1 << y
        mask_x = 1 << x
        h[y] |= mask_x
        v[x] |= mask_y
        if h[y] == 31 or v[x] == 31:
            print(f"{i} BOARD WIN SCORE: {calc_score(BOARDS[i], h, num)}")
            WON_BOARDS[i] = True
