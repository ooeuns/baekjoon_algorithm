import sys


def possible(num: str, lost_num: set):
    for n in num:
        if n in lost_num:
            return 0
    return len(num)


def solution(N: int, lost_num: set):
    ans = abs(N - 100)

    for num in range(1000001):
        str_num = str(num)
        l = possible(str_num, lost_num)

        if l:
            ans = min(ans, l + abs(N-num))
    return ans


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())

    if M:
        lost_num = set(map(str, sys.stdin.readline().split()))
    else:
        lost_num = set()

    print(solution(N, lost_num))
