f = '1.in'
D = open(f).read().strip()
R = [int(line) for line in D.splitlines()]

ans1 = 0
for a, b in zip(R, R[1:]):
    if a < b:
        ans1 += 1
print(ans1)


ans2 = 0
S = [a + b + c for a, b, c in zip(R, R[1:], R[2:])]
for a, b in zip(S, S[1:]):
    if a < b:
        ans2 += 1
print(ans2)