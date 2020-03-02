import sys


def solution(time_table: list):
    ans = 0
    start = 0

    for time in time_table:
        str_time, end_time = time

        if str_time >= start:
            start = end_time
            ans += 1
    return ans


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    time_table = [tuple(map(int, sys.stdin.readline().split()))
                  for _ in range(N)]
    print(solution(sorted(time_table, key=lambda x: (x[1], x[0]))))
