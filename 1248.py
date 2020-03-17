import sys
from collections import deque


def check(index):
    s = 0
    for i in range(index, -1, -1):
        s += ans[i]
        if matrix[i][index] == 0:
            if s != 0:
                return False
        elif matrix[i][index] < 0:
            if s >= 0:
                return False
        elif matrix[i][index] > 0:
            if s <= 0:
                return False
    return True


def go(idx: int, n: int):
    global ans

    if idx == n:
        return True

    if matrix[idx][idx] == 0:
        ans[idx] = 0
        return check(idx) and go(idx+1, n)

    for i in range(1, 11):
        ans[idx] = matrix[idx][idx] * i
        if check(idx) and go(idx+1, n):
            return True
    return False


if __name__ == "__main__":
    # initialization
    n = int(sys.stdin.readline())
    ans = [0] * n

    operation = sys.stdin.readline().strip()
    matrix = [[0] * n for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(i, n):
            tmp = 0
            if operation[cnt] == '0':
                matrix[i][j] = 0
            elif operation[cnt] == '+':
                matrix[i][j] = 1
            else:
                matrix[i][j] = -1
            cnt += 1

    go(0, n)
    print(*ans)
