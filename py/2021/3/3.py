f = '3.in'
D = open(f).read().strip()
R = [line for line in D.splitlines()]
print(R)

N = len(R)
S = len(R[0])
gamma = 0
epsilon = 0
for i in range(S):
    cnt = [0, 0]
    for j in range(N):
        cnt[int(R[j][i])] += 1
    gamma *= 2
    epsilon *= 2
    if cnt[0] > cnt[1]:
        epsilon += 1
    else:
        gamma += 1

print(gamma)
print(epsilon)
print(gamma * epsilon)

Rf = [x for x in R]
for i in range(S):
    cnt = [0, 0]
    Nf = len(Rf)
    if Nf == 1:
        break
    for j in range(Nf):
        cnt[int(Rf[j][i])] += 1
    if cnt[0] > cnt[1]:
        Rf = [x for x in Rf if x[i] == '0']
    else:
        Rf = [x for x in Rf if x[i] == '1']

oxygenRatingStr = Rf[0]
oxygenRating = 0
for i in range(S):
    oxygenRating *= 2
    oxygenRating += int(oxygenRatingStr[i])
print(oxygenRating)

Rf = [x for x in R]
for i in range(S):
    cnt = [0, 0]
    Nf = len(Rf)
    if Nf == 1:
        break
    for j in range(Nf):
        cnt[int(Rf[j][i])] += 1
    if cnt[0] <= cnt[1]:
        Rf = [x for x in Rf if x[i] == '0']
    else:
        Rf = [x for x in Rf if x[i] == '1']

co2RatingStr = Rf[0]
co2Rating = 0
for i in range(S):
    co2Rating *= 2
    co2Rating += int(co2RatingStr[i])
print(co2Rating)
print(co2Rating * oxygenRating)