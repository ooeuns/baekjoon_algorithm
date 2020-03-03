import sys
from functools import reduce


def solution(formula: list):
    for i, v in enumerate(formula):
        if '+' in v:
            v = v.split('+')
            formula[i] = sum(map(int, v))
    return reduce(lambda x, y: x - y, map(int, formula))


if __name__ == "__main__":
    formula = list(sys.stdin.readline().strip().split('-'))
    print(solution(formula))
