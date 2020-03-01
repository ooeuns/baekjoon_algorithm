import sys

ans = float('-inf')


def dfs(cur_day: int, N: int, money: int, works: list):
    if cur_day == N:
        global ans
        ans = max(ans, money)
        return

    period, pay = works[cur_day]

    if cur_day + period > N:
        dfs(cur_day+1, N, money, works)
    else:
        dfs(cur_day+period, N, money+pay, works)
        dfs(cur_day+1, N, money, works)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    works = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

    dfs(0, N, 0, works)
    print(ans)
