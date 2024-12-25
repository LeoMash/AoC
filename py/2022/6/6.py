import sys

INPUT = "6.in"

def detect(s, l):
    if len(s) < l:
        return -1

    i = l
    while i < len(s):
        wnd = s[i - l:i]
        u = set(wnd)
        if len(u) == l:
            return i
        i += 1
    return -1


def run():
    with open(INPUT) as f:
        line = f.readline().strip()
        i4 = detect(line, 4)
        print(i4)
        i14 = detect(line, 14)
        print(i14)


def main():
    assert detect('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4) == 7
    assert detect('bvwbjplbgvbhsrlpgdmjqwftvncz', 4) == 5
    assert detect('nppdvjthqldpwncqszvftbrmjlhg', 4) == 6
    assert detect('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4) == 10
    assert detect('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4) == 11

    assert detect('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14) == 19
    assert detect('bvwbjplbgvbhsrlpgdmjqwftvncz', 14) == 23
    assert detect('nppdvjthqldpwncqszvftbrmjlhg', 14) == 23
    assert detect('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14) == 29
    assert detect('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14) == 26

    run()

    return 0


if __name__ == '__main__':
    sys.exit(main())
