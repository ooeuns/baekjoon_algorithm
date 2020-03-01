import sys
from math import gcd


def solution(M: int, N: int, x: int, y: int):
    lcm = M * N // gcd(M, N)
    x -= 1
    y -= 1

    for idx in range(x, lcm, M):
        if idx % N == y:
            return idx + 1
    return -1


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        M, N, x, y = map(int, sys.stdin.readline().split())
        print(solution(M, N, x, y))
