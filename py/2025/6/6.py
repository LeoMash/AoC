f = '6.in'
f = '6_test.in'
D = open(f).read()
OR = [line for line in D.splitlines()]
N = len(OR) - 1

OPS = OR[-1].split()
print(OPS)
K = len(OPS)
print(K)

R = OR[:-1]
print(R)

ans1 = 0
NUMS = []
for r in R:
    nums = [int(x) for x in r.split()]
    NUMS.append(nums)

print(NUMS)
for i in range(K):
    if OPS[i] == '+':
        r = 0
        for j in range(N):
            r += NUMS[j][i]
        ans1 += r
    else:
        r = 1
        for j in range(N):
            r *= NUMS[j][i]
        ans1 += r
print(ans1)

ans2 = 0

SN = len(R[0])

# opidx = 0
NUMS2 = []
curcol = []
for i in range(SN):
    col = []
    for j in range(N):
        x = OR[j][i]
        if x != ' ':
            col.append(x)
    s = ''.join(col).strip()
    if s:
        curcol.append(int(s))
    else:
        NUMS2.append(curcol)
        # op = OPS[opidx]
        # print(op, curcol)
        # opidx += 1
        curcol = []
NUMS2.append(curcol)

# print(len(NUMS2))
# print(K)
print(NUMS2)
assert len(NUMS2) == K

for i in range(K):
    if OPS[i] == '+':
        r = 0
        for n in NUMS2[i]:
            r += n
    else:
        r = 1
        for n in NUMS2[i]:
            r *= n
    ans2 += r

print(ans2)
