import sys


def solution(students: list, spv: int, sub_spv: int):
    ans = N
    students = list(map(lambda x: x-spv, students))

    for stu in students:
        if stu > 0:
            ans += stu // sub_spv
            if stu % sub_spv:
                ans += 1
    return ans


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    students = list(map(int, sys.stdin.readline().split()))
    spv, sub_spv = map(int, sys.stdin.readline().split())

    print(solution(students, spv, sub_spv))
