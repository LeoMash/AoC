
f = '1.in'
D = open(f).read().strip()
R = [int(line) for line in D.splitlines()]
R = [r // 3 - 2 for r in R]
ans1 = sum(R)
print(ans1)

ans2 = 0
for r in R:
    while r > 0:
        ans2 += r
        r = r // 3 - 2
print(ans2)