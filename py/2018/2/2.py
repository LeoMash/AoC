from collections import defaultdict

# f = '2_test2.in'
f = '2.in'
D = open(f).read().strip()
R = [line for line in D.splitlines()]

c2 = 0
c3 = 0
for r in R:
    d = defaultdict(int)
    for c in r:
        d[c] += 1
    # print(d)
    dd = defaultdict(int)
    for k, v in d.items():
        dd[v] += 1
    if dd[2] > 0:
        c2 += 1
    if dd[3] > 0:
        c3 += 1

ans1 = c2 * c3
print(ans1)


n = len(R)
l = len(R[0])
for i in range(n - 1):
    r1 = R[i]
    for j in range(1, n):
        r2 = R[j]
        idx = []
        for k in range(l):
            if r1[k] != r2[k]:
               idx.append(k)
        if len(idx) == 1:
            print(r1[:idx[0]], r1[idx[0]+1:])
            exit(0)