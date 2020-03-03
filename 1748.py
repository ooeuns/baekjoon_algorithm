import sys


def solution(num: int):
    ans = 0
    str_num = 1
    length = 1

    while str_num <= num:
        end_num = str_num * 10 - 1

        if end_num > num:
            end_num = num

        ans += (end_num - str_num + 1) * length

        str_num *= 10
        length += 1
    return ans


if __name__ == "__main__":
    num = int(sys.stdin.readline())
    print(solution(num))
