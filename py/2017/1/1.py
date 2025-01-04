f = '1.in'
D = open(f).read().strip()
print(D)

ans1 = 0
for i, c in enumerate(D):
    if D[i] == D[i - 1]:
        ans1 += int(D[i])
print(ans1)

ans2 = 0
for i, c in enumerate(D):
    if D[i] == D[i - len(D) // 2]:
        ans2 += int(D[i])
print(ans2)