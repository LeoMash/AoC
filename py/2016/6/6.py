from collections import Counter

f = '6.in'
D = open(f).read().strip()

R = []
for line in D.splitlines():
    R.append(line.strip())

N = len(R[0])

cnt = [Counter() for _ in range(N)]
for r in R:
    for i,c in enumerate(r):
        cnt[i][c] += 1

ans1 = ''
ans2 = ''
for cn in cnt:
    lst = cn.most_common(len(cn))
    ans1 += lst[0][0]
    ans2 += lst[-1][0]
print(ans1)
print(ans2)