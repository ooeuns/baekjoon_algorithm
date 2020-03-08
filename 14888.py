import sys


def dfs(num: int, idx: int, add: int, sub: int, multi: int, division: int):
    if idx == N:
        global maxv, minv
        maxv = max(maxv, num)
        minv = min(minv, num)
        return

    if add:
        dfs(num + numbers[idx], idx+1, add-1, sub, multi, division)
    if sub:
        dfs(num - numbers[idx], idx+1, add, sub-1, multi, division)
    if multi:
        dfs(num * numbers[idx], idx+1, add, sub, multi-1, division)
    if division:
        dfs(int(num / numbers[idx]), idx+1, add, sub, multi, division-1)


if __name__ == "__main__":
    maxv, minv = float('-inf'), float('inf')

    N = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    add, sub, multi, division = map(int, sys.stdin.readline().split())

    dfs(numbers[0], 1, add, sub, multi, division)
    print(maxv)
    print(minv)
