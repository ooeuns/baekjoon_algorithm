import sys


def dfs(cur_day: int, N: int, money: int, works: list):
    if cur_day == N:
        return money

    period, pay = works[cur_day]

    if cur_day + period > N:
        return dfs(cur_day+1, N, money, works)
    else:
        return max(dfs(cur_day+period, N, money+pay, works),
                   dfs(cur_day+1, N, money, works))


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    works = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(dfs(0, N, 0, works))
