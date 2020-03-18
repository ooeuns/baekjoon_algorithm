import sys

ans = 0


def is_possible(x: int):
    for i in range(x):
        if row[i] == row[x] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def dfs(x: int):
    global ans

    if x == N:
        ans += 1
    else:
        for i in range(N):
            row[x] = i
            if is_possible(x):
                dfs(x+1)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    row = [0] * N

    dfs(0)
    print(ans)
