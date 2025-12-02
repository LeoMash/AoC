f = '2.in'
# f = '2_test.in'
D = open(f).read().strip()
D = ''.join(D.splitlines())

P = []
for pair in D.split(','):
    b, e = pair.split('-')
    P.append((int(b), int(e)))
print(P)

# def is_valid(x, n):
#     if n % 2 != 0:
#         return True
#     if x[:n//2] == x[n//2:]:
#         return False
#     return True

def is_valid_p(x, n, p):
    if n % p != 0:
        return True
    pl = n // p
    fp = x[:pl]
    for ii in range(1, p):
        xp = x[ii * pl:(ii + 1) * pl]
        if fp != xp:
            return True
    return False


def is_valid2(x, n):
    for p in range(2, n + 1):
        if not is_valid_p(x, n, p):
            return False
    return True


ans1 = 0
ans2 = 0

for b, e in P:
    for i in range(b, e + 1):
        x = str(i)
        n = len(x)
        if not is_valid_p(x, n, 2):
            ans1 += i
        if not is_valid2(x, n):
            ans2 += i
print(ans1)
print(ans2)
