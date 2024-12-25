import sys


def run(argc, argv):
    with open('1.in') as f:
        arr = []
        cursum = 0
        for line in f:
            line = line.strip()
            if not line:
                arr.append(cursum)
                cursum = 0
            else:
                cursum += int(line)
        arr.append(cursum)

        arr = sorted(arr)
        print(arr)
        print(arr[-3:])
        print(sum(arr[-3:]))

    pass


if __name__ == '__main__':
    sys.exit(run(len(sys.argv), sys.argv))
