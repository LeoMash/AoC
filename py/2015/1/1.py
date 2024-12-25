f = '1.in'
D = open(f).read().strip()

ans1 = 0
ans2 = 0
for i, c in enumerate(D):
    if c == '(':
        ans1 += 1
    else:
        ans1 -= 1
        if ans2 == 0 and ans1 < 0:
            ans2 = i
print(ans1)
print(ans2 + 1)
