import sys
import re

# INPUT = "5test.in"
INPUT = "5.in"

MOVE_MATCH = re.compile(r"move (\d+) from (\d+) to (\d+)")


def apply_move(stacks, move):
    num, i_from, i_to = move
    i_from -= 1
    i_to -= 1
    stacks[i_to] += reversed(stacks[i_from][-num:])
    del stacks[i_from][-num:]


def apply_move9001(stacks, move):
    num, i_from, i_to = move
    i_from -= 1
    i_to -= 1
    stacks[i_to] += stacks[i_from][-num:]
    del stacks[i_from][-num:]


def run1(argc, argv):
    with open(INPUT) as f:
        n = int(f.readline())
        stacks = []
        for i in range(n):
            line = f.readline()
            line = line.strip()
            stacks.append(list(line))

        print(stacks)
        for line in f:
            line = line.strip()
            if not line:
                continue
            move = map(int, MOVE_MATCH.match(line).groups())
            # apply_move(stacks, move)
            apply_move9001(stacks, move)
            print(stacks)
        print(stacks)
        ans = ''
        for st in stacks:
            if st:
                ans += st[-1]
            else:
                ans += ' '
        print(ans)


if __name__ == '__main__':
    sys.exit(run1(len(sys.argv), sys.argv))
