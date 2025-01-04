f = '2.in'
D = open(f).read().strip()
R = []
for line in D.splitlines():
    nums = [int(x) for x in line.split()]
    R.append(nums)

ans1 = sum([max(r) - min(r) for r in R])
print(ans1)

def find_div(rs):
    for i in range(len(rs) - 1):
        for j in range(i + 1, len(rs)):
            if rs[j] % rs[i] == 0:
                return rs[j] // rs[i]
    assert False

ans2 = 0
for r in R:
    rs = sorted(r)
    ans2 += find_div(rs)
print(ans2)
