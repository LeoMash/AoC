f = '8.in'
K = 1000
# f = '8_test.in'
# K = 10
D = open(f).read().strip()

F = [list(map(int, line.split(','))) for line in D.splitlines()]
N = len(F)

print(F)
print(N)

def dst2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2

DST = []
for i in range(N - 1):
    for j in range(i + 1, N):
        DST.append((dst2(F[i], F[j]), i, j))

print(DST)

DST.sort()
print(DST)

# print(F[DST[0][1]])
# print(F[DST[0][2]])
# print(F[DST[1][1]])
# print(F[DST[1][2]])

UF = list(range(N))
SZ = [1] * N

def find(u):
    root = UF[u]
    if UF[root] != root:
        UF[u] = find(root)
        return UF[u]
    return root

def unite(u, v):
    uu = find(u)
    vv = find(v)
    if uu == vv:
        return None
    usize = SZ[uu]
    vsize = SZ[vv]
    if usize < vsize:
        UF[uu] = vv
        SZ[vv] += SZ[uu]
        if SZ[vv] == N:
            return u, v
    else:
        UF[vv] = uu
        SZ[uu] += SZ[vv]
        if SZ[uu] == N:
            return u, v


for i in range(K):
    unite(DST[i][1], DST[i][2])

print(UF)
print(SZ)

sets = set()
for i in range(N):
    ii = find(i)
    sets.add((ii, SZ[ii]))

print(len(sets))
print(sets)

szsorted = []
for _, sz in sets:
    szsorted.append(sz)
szsorted = list(reversed(sorted(szsorted)))
ans1 = 1
for i in range(3):
    ans1 *= szsorted[i]
print(ans1)

ans2 = 0
for i in range(K, N ** 2):
    p = unite(DST[i][1], DST[i][2])
    if p is not None:
        u, v = p
        print(u, v)
        print(F[u], F[v])
        ans2 = F[u][0] * F[v][0]
        break

print(ans2)
