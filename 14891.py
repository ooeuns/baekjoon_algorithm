import sys


def chk_pos(idx: int):
    if idx > 7:
        return idx - 8
    elif idx < 0:
        return 8 - abs(idx)
    else:
        return idx


def mv_saw(idx: int, direction: int):
    if idx < 0 or idx >= 3:
        return

    sign[idx] = chk_pos(sign[idx] + direction)
    right = chk_pos(sign[idx] + 2)
    left = chk_pos(sign[idx]-2)

    if saw_tooth[sign[idx][right]] != saw_tooth[sign[idx+1][left]]:
        sign[idx+1] = -chk_pos(sign[idx] + direction)
    return


def solution(k: int, v: int):
    mv = 1 if v > 0 else -1
    for _ in range(abs(v)):
        mv_saw(k, mv)
        mv_saw(k-1, mv)


if __name__ == "__main__":
    saw_tooth = [list(map(int, sys.stdin.readline().split()))
                 for _ in range(4)]
    sign = [0] * 4
    K = int(sys.stdin.readline())
    for _ in range(K):
        k, v = map(int, sys.stdin.readline().split())
        solution(k, v)

    print(sign)
