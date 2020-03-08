import sys
from itertools import combinations

chk = False
while True:
    lst = list(map(int, sys.stdin.readline().split()))

    if lst[0] == 0:
        break
    if chk:
        print()

    k = lst[0]
    numbers = lst[1:]

    combi = list(map(sorted, combinations(numbers, 6)))
    for c in combi:
        print(*c)

    chk = True
