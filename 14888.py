import sys
from itertools import permutations


ans = []


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    ex_operation = list(sys.stdin.readline().strip().split())

    operation = []
    operation.extend(['+' for _ in range(ex_operation[0])])
    operation.extend(['-' for _ in range(ex_operation[1])])
    operation.extend(['*' for _ in range(ex_operation[2])])
    operation.extend(['//' for _ in range(ex_operation[3])])
