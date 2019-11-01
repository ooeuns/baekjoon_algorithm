import sys


def solution(h, m):
    m = m - 45
    if m < 0:
        m = 60 - abs(m)
        h -= 1

    if h < 0:
        h = 24 - abs(h)

    print("{} {}".format(h, m))

if __name__ == "__main__":
    h, m = map(int, sys.stdin.readline().split())
    solution(h, m)
