f = '2.in'
D = open(f).read().strip()

ans1 = 0
ans2 = 0
for line in D.splitlines():
    box = line.split('x')
    box = list(sorted(map(int, box)))
    frames = [box[0] * box[1], box[0] * box[2], box[1] * box[2]]
    vol = box[0] * box[1]  * box[2]
    ans1 += sum(frames) * 2 + frames[0]
    ans2 += vol + 2 * (box[0] + box[1])

print(ans1)
print(ans2)
