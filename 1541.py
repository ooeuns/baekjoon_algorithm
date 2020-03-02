import sys


def mk_formula(ex_formula: str):
    formula = []
    tmp = ''

    for oper in ex_formula:
        if oper in ('+', '-'):
            formula.append(int(tmp))
            formula.append(oper)
            tmp = ''
        else:
            tmp += oper

    formula.append(int(tmp))
    return formula


def solution(formula: list):
    lst = []
    for oper in formula:
        if oper == '+':
            lst.pop()

    return formula


if __name__ == "__main__":
    ex_formula = list(sys.stdin.readline())
    formula = mk_formula(ex_formula)

    print(solution(formula))
