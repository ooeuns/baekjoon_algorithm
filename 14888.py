import sys
from itertools import permutations


def calculation(i: int, j: int, k: str):
    if k == '+':
        return i + j
    elif k == '-':
        return i - j
    elif k == '/':
        return int(i / j)
    elif k == '*':
        return i * j


def dfs(cur_node: int, ans: int):
    if cur_node == len(operation):
        global mx
        global mn

        if ans > mx:
            mx = ans
        if ans < mn:
            mn = ans
    else:
        for i in range(len(operation)):
            if not visited[i]:
                visited[i] = True
                dfs(cur_node+1, calculation(ans, numbers[i+1], operation[i]))
                visited[i] = False


if __name__ == "__main__":
    visited = [False] * 12
    mx, mn = -1000000000, 1000000000

    N = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    ex_operation = list(map(int, sys.stdin.readline().split()))

    operation = []
    operation.extend(['+' for _ in range(ex_operation[0])])
    operation.extend(['-' for _ in range(ex_operation[1])])
    operation.extend(['*' for _ in range(ex_operation[2])])
    operation.extend(['/' for _ in range(ex_operation[3])])

    for i in range(len(operation)):
        visited[i] = True
        dfs(1, calculation(numbers[0], numbers[1], operation[i]))
        visited[i] = False

    print(mx)
    print(mn)
