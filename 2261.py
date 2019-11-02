import sys
import bisect
from itertools import combinations


def distance(pmt):
    return ((pmt[0][0] - pmt[1][0]) ** 2) + ((pmt[0][1] - pmt[1][1]) ** 2)

def compare_x(pmt):
    return (pmt[0][0] - pmt[1][0]) ** 2

# def compare_y(pmt):

def filter_x(number_of_cases, d):
    
    x = []
    for case in number_of_cases:
        if d > compare_x(case):
            x.append(case)
    return x
    
def filter_y(number_of_cases, d):
    number_of_cases.sort(key = lambda x:x[1]) # y 기준으로 정렬
    start = bisect.bisect_left(number_of_cases, lambda y: y[0][1]-b or y[1][]-b)
    end = bisect.bisect_left(number_of_cases, y+d)

def solution(points):
    number_of_cases = list(combinations(points, 2))

    number_of_cases.sort(key = lambda x:x[0])   # x 기준으로 정렬
    d = distance(number_of_cases[0])

    x = filter_x(number_of_cases, d)
    




if __name__ == "__main__":
    T = int(sys.stdin.readline())
    points = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
    print(solution(points))



    # points = [[1, 0], [2, -10], [3, 10], [4, 0]]
    # print(solution(points))
    # points = [[10, 10], [0, 0], [10, 0], [0, 10]]
    # print(solution(points))
    
