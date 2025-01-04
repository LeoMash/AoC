from collections import defaultdict

f = '4.in'
D = open(f).read().strip()

ans1 = 0
ans2 = 0
for line in D.splitlines():
    words = line.split()
    words_set = set(words)
    if len(words_set) == len(words):
        ans1 += 1
    words_ordered = [str(sorted(word)) for word in words]
    words_ordered_set = set(words_ordered)
    if len(words_ordered_set) == len(words_ordered):
        ans2 +=1
print(ans1)
print(ans2)