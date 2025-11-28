from collections import defaultdict

f = '6.in'
D = open(f).read().strip()
L = list(map(int, D.split(',')))
print(L)
M = defaultdict(int)
for l in L:
    M[l] += 1
print(M)

DAYS1 = 80
for d in range(DAYS1):
    n = M[0]
    for i in range(0, 8):
        M[i] = M[i + 1]
    M[8] = n
    M[6] += n
    # print(M)

ans1 = 0
for k, v in M.items():
    ans1 += v
print(ans1)

DAYS2 = 256
for d in range(DAYS1, DAYS2):
    n = M[0]
    for i in range(0, 8):
        M[i] = M[i + 1]
    M[8] = n
    M[6] += n

ans2 = 0
for k, v in M.items():
    ans2 += v
print(ans2)
