import sys


def next_year(M: int, N: int, cur_year: tuple):
    cur_year = tuple(map(lambda x: x+1, cur_year))
    x, y, cnt = cur_year

    if x > M:
        x = 1
    if y > N:
        y = 1

    return (x, y, cnt)


def solution(M: int, N: int, x: int, y: int):
    cur_year = (1, 1, 1)

    while True:
        cur_x, cur_y, cnt = cur_year
        if cur_x == x and cur_y == y:
            return cnt
        elif cur_x == M and cur_y == N:
            return -1

        cur_year = next_year(M, N, (cur_x, cur_y, cnt))


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        M, N, x, y = map(int, sys.stdin.readline().split())
        print(solution(M, N, x, y))
