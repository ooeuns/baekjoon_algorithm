import sys

pkg = {
    '(': ')',
    '[': ']'
}


def solution(brackets: str):
    brackets = brackets.replace('()', '2')
    brackets = brackets.replace('[]', '3')

    stack = []
    for bracket in brackets:
        if bracket in pkg.keys():
            stack.append(bracket)


if __name__ == "__main__":
    brackets = sys.stdin.readline().strip()
    print(solution(brackets))
