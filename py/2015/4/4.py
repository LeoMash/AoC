import hashlib

f = '4.in'
D = open(f).read().strip()

i = 0
while True:
    s = D + str(i)
    md5 = hashlib.md5(s.encode()).hexdigest()
    if md5.startswith('00000'):
        break
    i += 1
print(i)

while True:
    s = D + str(i)
    md5 = hashlib.md5(s.encode()).hexdigest()
    if md5.startswith('000000'):
        break
    i += 1
print(i)
