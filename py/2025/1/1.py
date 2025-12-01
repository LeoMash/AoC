f = '1.in'
# f = '1_test.in'
D = open(f).read().strip()
R = [(line[0], int(line[1:])) for line in D.splitlines()]

ans1 = 0
ans2 = 0
num  = 50
for d, r in R:
    # print(d, r)

    sgn = 1 if d == 'R' else -1

    full = r // 100
    rr = sgn * (r % 100)
    ans2 += full

    if num != 0:
        if num + rr <= 0:
            ans2 += 1
        elif num + rr > 99:
            ans2 += 1
    num += sgn * r
    num %= 100
    if (num == 0):
        ans1 += 1
    # print(num)
    # print(ans2)

print(ans1)
print(ans2)
