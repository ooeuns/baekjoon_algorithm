import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
numbers = [x for x in range(1, N+1)]

combi = list(map(sorted, combinations(numbers, M)))
for c in combi:
    print(*c)
