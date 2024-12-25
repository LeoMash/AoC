import sys


def run1(argc, argv):
    with open("3.in") as f:
        score = 0
        for line in f:
            line = line.strip()
            l = len(line) // 2
            a = line[:l]
            b = line[l:]
            set_a = set(a)
            set_b = set(b)
            un = list(set_a & set_b)
            d = un[0]
            if 'a' <= d <= 'z':
                score += ord(d) - ord('a') + 1
            else:
                score += ord(d) - ord('A') + 27

        print(score)

    pass


def run2(argc, argv):
    with open("3.in") as f:
        score = 0
        group = []
        for line in f:
            line = line.strip()
            group.append(line)
            if len(group) == 3:
                a = group[0]
                b = group[1]
                c = group[2]
                set_a = set(a)
                set_b = set(b)
                set_c = set(c)
                un = list(set_a & set_b & set_c)
                d = un[0]
                if 'a' <= d <= 'z':
                    score += ord(d) - ord('a') + 1
                else:
                    score += ord(d) - ord('A') + 27

                group = []

        print(score)

    pass


if __name__ == '__main__':
    sys.exit(run2(len(sys.argv), sys.argv))
