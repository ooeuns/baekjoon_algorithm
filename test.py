import sys
from itertools import combinations


def solution(points):
    permutation = list(combinations(points, 2))

    minimum = float('inf')
    for pmt in permutation:
        ab = ((pmt[0][0] - pmt[1][0]) ** 2) + ((pmt[0][1] - pmt[1][1]) ** 2)
        if ab < minimum:
            minimum = ab
    
    return minimum

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    points = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]

    # points = [[1, 0], [2, -10], [3, 10], [4, 0]]
    print(solution(points))