import sys


def all_btn_broken(remote_ctrl: list):
    if True not in remote_ctrl:
        return False


def find_num(num: int, direc: int, remote_ctrl: list):
    if num < 0 or num > 9:
        return float('inf')

    if remote_ctrl[num]:
        return num
    elif not remote_ctrl[num]:
        return find_num(num + direc, direc, remote_ctrl)


def find_near_num(N: int, remote_ctrl: list):
    near_num = []
    numbers = list(map(int, list(str(N))))

    for num in numbers:
        near_num.append(min(find_num(num, 1, remote_ctrl),
                            find_num(num, -1, remote_ctrl)))
    return int(''.join(list(map(str, near_num))))


def solution(N: int, lost_num: list):
    if N == 100:
        return 0

    remote_ctrl = [True] * 10
    for num in lost_num:
        remote_ctrl[num] = False
    if all_btn_broken(remote_ctrl):
        return abs(N - 100)

    near_num = find_near_num(N, remote_ctrl)

    return abs(N - near_num) + len(str(N))


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    lost_num = list(map(int, sys.stdin.readline().split()))

    print(solution(N, lost_num))
