import re
import sys

INPUT = "4.in"

RANGE_MATCH = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")


def overlapped(r):
    if r[0] <= r[2] and r[1] >= r[3]:
        return True
    if r[2] <= r[0] and r[3] >= r[1]:
        return True
    return False


def intersected(r):
    if r[1] < r[2]:
        return False
    if r[3] < r[0]:
        return False
    return True


def run1(argc, argv):
    with open(INPUT) as f:
        cnt_overlapped = 0
        cnt_intersected = 0
        for line in f:
            line = line.strip()
            m = RANGE_MATCH.match(line)
            r = [int(m.group(i)) for i in range(1, 5)]
            cnt_overlapped += overlapped(r)
            cnt_intersected += intersected(r)

        print(cnt_overlapped)
        print(cnt_intersected)


if __name__ == '__main__':
    sys.exit(run1(len(sys.argv), sys.argv))
