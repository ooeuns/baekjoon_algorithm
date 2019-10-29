import sys

OPEN = "("
CLOSE = ")"
operator = {"+", "-", "*", "/", OPEN, CLOSE}

def priority(oprt):
    if oprt == '*' or oprt == '/':
        return 9
    elif oprt == '+' or oprt == '-':
        return 7
    elif oprt == '(' or oprt == ')':
        return 5
    else:
        return -1

def solution(notations):
    ans = []
    stack = []

    for notation in notations:
        if notation == OPEN:
            stack.append(OPEN)
        elif notation == CLOSE:
            while True:
                check = stack.pop()
                if check == OPEN:
                    break
                ans.append(check)
        elif notation not in operator:
            ans.append(notation)
        elif notation in operator:
            if stack and priority(stack[-1]) < priority(notation):
                stack.append(notation)
            else:
                while stack and priority(stack[-1]) >= priority(notation):
                    ans.append(stack.pop())
                stack.append(notation)


    while stack: ans.append(stack.pop())
    return ''.join(ans)
        

if __name__ == "__main__":
    notations = sys.stdin.readline().strip()
    print(solution(notations))

    # autu checking
    # print(solution("(A+(B*C))-(D/E)"))  # ABC*+DE/-
    # print(solution("A*(B+C)"))  # ABC+*
    # print(solution("A+(B*C)*D*E+F"))    # ABC*D*E*+F+