import sys
from collections import Counter
from string import ascii_lowercase


def solution(ss: str):
    ss = Counter(ss)
    lst = []
    for a in ascii_lowercase:
        lst.append(ss[a])
    print(*lst)


if __name__ == "__main__":
    ss = sys.stdin.readline().strip()
    solution(ss)
