f = '7.in'
# f = '7_test.in'
D = open(f).read().strip()

F = []
for line in D.splitlines():
    F.append([x for x in line])

N = len(F)
M = len(F[0])

# print(F)
print(N, M)

def find_s():
    for i in range(N):
        for j in range(M):
            if F[i][j] == 'S':
                return i, j
    return None, None
sx, sy = find_s()
print(sx, sy)

ans1 = 0
def go(x, y):
    if x == N or y < 0 or y >= M:
        return
    c = F[x][y]
    if c == '|':
        return
    if c == '^':
        go(x, y - 1)
        go(x, y + 1)
        global ans1
        ans1 += 1
    else:
        F[x][y] = '|'
        go(x + 1, y)

go(sx, sy)

# for line in F:
#     print(line)

print(ans1)

memo = {}
def w(x, y):
    if (x, y) in memo:
        return memo[(x, y)]
    if x + 1 == N:
        weight = 1
    else:
        if F[x + 1][y] == '^':
            weight =  (w(x + 1, y - 1) +
                       w(x + 1, y + 1))
        else:
            weight =  w(x + 1, y)
    memo[(x, y)] = weight
    return weight

ans2 = w(sx, sy)
print(ans2)
