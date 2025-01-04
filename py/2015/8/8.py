f = '8.in'
D = open(f).read().strip()

ans = sum(len(line) - len(eval(line)) for line in D.splitlines())
ans2 = sum(2 + line.count('\\') + line.count('"') for line in D.splitlines())
print(ans)
print(ans2)

