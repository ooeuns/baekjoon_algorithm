import sys
from itertools import combinations


def cal_score(team: list, matrix: list):
    ans = 0
    for i in team:
        for j in team:
            ans += matrix[i][j]
    return ans


def solution(combi: list, numbers: set):
    ans = float('inf')
    for c in combi:
        ans = min(ans, abs(cal_score(c, matrix) -
                           cal_score(list(numbers - set(c)), matrix)))

    return ans


if __name__ == "__main__":
    row = int(sys.stdin.readline())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]

    numbers = [x for x in range(row)]
    combi = list(combinations(numbers, row//2))
    print(solution(combi, set(numbers)))
