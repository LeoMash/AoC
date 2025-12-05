f = '5.in'
# f = '5_test.in'
D = open(f).read().strip()
D1, D2 = D.split('\n\n')
R = [list(map(int, line.split('-'))) for line in D1.splitlines()]
# print(R)

IDS = [int(line) for line in D2.splitlines()]
# print(IDS)

ans1 = 0
for id in IDS:
    for a, b in R:
        if a <= id <= b:
            ans1 += 1
            break
print(ans1)

RS = list(sorted(R))
# print(RS)

ans2 = 0
cur = -1
for a, b in RS:
    if a <= cur:
        a = cur + 1
    if a <= b:
        cur_len = b - a + 1
        ans2 += cur_len
    cur = max(cur, b)

print(ans2)
