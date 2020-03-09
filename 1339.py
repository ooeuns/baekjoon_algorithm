import sys
from collections import deque
from itertools import permutations


def solution(words: list):
    return words


if __name__ == "__main__":
    ALPHA = [x for x in range(10)]

    N = int(sys.stdin.readline())
    words = list(sys.stdin.readline().strip() for _ in range(N))

    print(solution(sorted(words, key=lambda x: len(x), reverse=True)))
