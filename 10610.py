import sys
from itertools import permutations


def solution(number: str):
    if '0' not in number:
        return -1
    if sum(map(int, number)) % 3 != 0:
        return -1
    return ''.join(sorted(number, reverse=True))


if __name__ == "__main__":
    number = sys.stdin.readline().strip()
    print(solution(number))
