from collections import Counter

f = '4.in'
D = open(f).read().strip()

R = []
for line in D.splitlines():
    idx = line.index('[')
    passw = line[:idx]
    parts = passw.split('-')
    passw = ''.join(parts[:-1])
    num = int(parts[-1])
    checksum = line[idx+1:-1]
    R.append((passw, num, checksum))
print(R)

ans1 = 0
for passw, num, checksum in R:
    passw = list(passw)
    passw.sort()
    cnt = Counter(passw)
    cmn = cnt.most_common(5)
    s = ''.join([c for c, ccnt in cmn])
    if s == checksum:
        ans1 += num
print(ans1)

for passw, num, checksum in R:
    passw = list(passw)
    passw_enc = ''.join([chr(ord('a') + (ord(c) - ord('a') + num) % 26) for c in passw])
    if 'northpole' in passw_enc:
        print(passw_enc, num)
        break