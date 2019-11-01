import sys
from itertools import combinations


def distance(pmt):
    return ((pmt[0][0] - pmt[1][0]) ** 2) + ((pmt[0][1] - pmt[1][1]) ** 2)
    
def solution(points):
    if len(points) > 5:
        points.sort(key = lambda x:x[0])
        mid = len(points) // 2
        delta = (points[mid][0] + points[mid][0]) / 2
        
        if mid < delta:
            mid = int(delta)
        
        left_min = min(map(distance, combinations(points[:mid], 2)))
        right_min = min(map(distance, combinations(points[mid:], 2)))

        single = min(left_min, right_min)

        return min(left_min, right_min, single)

    else:
        return min(map(distance, combinations(points, 2)))

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    points = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
    print(solution(points))



    # points = [[1, 0], [2, -10], [3, 10], [4, 0]]
    # print(solution(points))
    # points = [[10, 10], [0, 0], [10, 0], [0, 10]]
    # print(solution(points))
    
