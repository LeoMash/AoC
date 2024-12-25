import hashlib

f = '5.in'
D = open(f).read().strip()

def is_nice(s):
    forbidden = {'ab', 'cd', 'pq', 'xy'}
    for f in forbidden:
        if f in s:
            return False

    vowels = 'aeiou'
    vow_num = 0
    has_twice_letter = False
    for i, c in enumerate(s):
        if c in vowels:
            vow_num += 1
        if i < len(s) - 1 and s[i] == s[i + 1]:
            has_twice_letter = True
    return has_twice_letter and vow_num >= 3

# print(is_nice('ugknbfddgicrmopn'))

def is_nice2(s):
    rule1 = False
    for i in range(len(s) - 1):
        ss = s[i:i + 2]
        if not rule1 and s[i + 2:].find(ss) >= 0:
            rule1 = True
    if not rule1:
        return False

    rule2 = False
    for i in range(len(s) - 2):
        if not rule2 and s[i] == s[i + 2]:
            rule2 = True
    if not rule2:
        return False
    return True

# print(is_nice2('qjhvhtzxzqqjkmpb'))
# print(is_nice2('xxyxx'))
# print(is_nice2('uurcxstgmygtbstg'))
# print(is_nice2('ieodomkazucvgmuy'))

ans1 = 0
ans2 = 0
for line in D.splitlines():
    ans1 += is_nice(line)
    ans2 += is_nice2(line)
print(ans1)
print(ans2)
