import sys
from itertools import combinations


points = [[1, 0], [2, -10], [3, 10], [4, 0], [-2, 3], [4, 7], [2, 7], [5, 6]]
mid = len(points) // 2


def distance(pmt):
    return ((pmt[0][0] - pmt[1][0]) ** 2) + ((pmt[0][1] - pmt[1][1]) ** 2)

def each_side(left, right):
    pair = []
    for l in left:
        for r in right:
            pair.append([l, r])
    return pair

print(min(map(distance, each_side(points[:mid], points[mid:]))))
