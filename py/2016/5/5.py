import hashlib

f = '5.in'
D = open(f).read().strip()

# D = 'abc'
i = 0
ans1 = ''
ans2 = ['_'] * 8

def filled(s):
    for c in s:
        if c == '_':
            return False
    return True

while len(ans1) < 8 or not filled(ans2):
    while True:
        s = D + str(i)
        md5 = hashlib.md5(s.encode()).hexdigest()
        if md5.startswith('00000'):
            print(i, s, md5)
            if len(ans1) < 8:
                ans1 += md5[5]
            if ord('0') <= ord(md5[5]) <= ord('7') and ans2[int(md5[5])] == '_':
                ans2[int(md5[5])] = md5[6]
            i += 1
            break
        i += 1
print(ans1)
print(''.join(ans2))