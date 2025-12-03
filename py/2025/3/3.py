f = '3.in'
# f = '3_test.in'
D = open(f).read().strip()
R = [line for line in D.splitlines()]

def maxrowval(r, k):
    x = [int(c) for c in r]
    res = 0
    while k > 0:
        n = len(x)
        maxx = 0
        maxi = 0
        for j in range(n - k + 1):
            if x[j] > maxx:
                maxx = x[j]
                maxi = j
        res = res * 10 + maxx
        x = x[maxi+1:]
        k -= 1
    return res

ans1 = 0
ans2 = 0
for r in R:
    maxr1 = maxrowval(r, 2)
    maxr2 = maxrowval(r, 12)
    # print(maxr1)
    # print(maxr2)
    ans1 += maxr1
    ans2 += maxr2

print(ans1)
print(ans2)
