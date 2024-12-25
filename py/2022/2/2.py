import sys

# A for Rock, B for Paper, and C for Scissors
#1 X for Rock, Y for Paper, and Z for Scissors
tbl1 = [
    [1 + 3, 2 + 6, 3 + 0],
    [1 + 0, 2 + 3, 3 + 6],
    [1 + 6, 2 + 0, 3 + 3],
]

#2 X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
tbl2 = [
    [3 + 0, 1 + 3, 2 + 6],
    [1 + 0, 2 + 3, 3 + 6],
    [2 + 0, 3 + 3, 1 + 6],
]


def match1(a, x):
    return tbl1[a][x]


def match2(a, x):
    return tbl2[a][x]


def run(argc, argv):
    with open("2.in") as f:
        score = 0
        for line in f:
            line = line.strip()
            a, b = line.split(' ')
            score += match2(ord(a) - ord('A'), ord(b) - ord('X'))

        print(score)

    pass


if __name__ == '__main__':
    sys.exit(run(len(sys.argv), sys.argv))
