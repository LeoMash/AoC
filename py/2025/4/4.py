f = '4.in'
# f = '4_test.in'
D = open(f).read().strip()
R = [line for line in D.splitlines()]

F = []
for line in R:
    F.append([x for x in line])
N = len(F)
M = len(F[0])
print(F)

DIR8 = [
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1],
    [-1, 0],
    [-1, 1],
]


ans1 = 0
for i in range(N):
    for j in range(M):
        if F[i][j] == '@':
            rc = 0
            for d in DIR8:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    if F[ni][nj] == '@':
                        rc += 1
            if rc < 4:
                ans1 += 1
print(ans1)


ans2 = 0
while True:
    num_removed = 0
    for i in range(N):
        for j in range(M):
            if F[i][j] == '@':
                rc = 0
                for d in DIR8:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < N and 0 <= nj < M:
                        if F[ni][nj] == '@':
                            rc += 1
                if rc < 4:
                    F[i][j] = '.'
                    ans2 += 1
                    num_removed += 1
    if num_removed == 0:
        break
print(ans2)
