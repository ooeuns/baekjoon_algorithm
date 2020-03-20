import sys
from collections import deque


def chk_right(idx: int, direction: int):
    if idx >= 3 or gears[idx][2] == gears[idx+1][6]:
        return

    chk_right(idx+1, -direction)
    gears[idx+1].rotate(direction)


def chk_left(idx: int, direction: int):
    if idx < 1 or gears[idx][6] == gears[idx-1][2]:
        return

    chk_left(idx-1, -direction)
    gears[idx-1].rotate(direction)


if __name__ == "__main__":
    gears = [deque(list(sys.stdin.readline().strip())) for _ in range(4)]
    T = int(sys.stdin.readline())

    for _ in range(T):
        idx, direction = map(int, sys.stdin.readline().split())
        idx -= 1

        chk_right(idx, -direction)
        chk_left(idx, -direction)
        gears[idx].rotate(direction)

    cnt = 1
    ans = 0
    for gear in gears:
        if gear[0] == '1':
            ans += cnt
        cnt *= 2

    print(ans)
