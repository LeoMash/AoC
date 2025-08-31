f = '1.in'
D = open(f).read().strip()
R = [int(line) for line in D.splitlines()]
CoR = {2020 - r for r in R}
for r in R:
    if r in CoR:
        print(r * (2020 - r))
        break

def part2():
    for i in range(len(R)):
        for j in range(i + 1, len(R)):
            for k in range(j + 1, len(R)):
                if R[i] + R[j] + R[k] == 2020:
                    print(R[i] * R[j] * R[k])
                    return
part2()
