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
        if notation == OPEN:    # 괄호가 열리면 무조건 push
            stack.append(OPEN)
        elif notation == CLOSE: # 괄호가 닫히면 열린 괄호가 나올때까지 pop
            while True:
                check = stack.pop()
                if check == OPEN:
                    break
                ans.append(check)
        elif notation not in operator:  # 숫자라면 출력
            ans.append(notation)
        elif notation in operator:  # 연산자라면 stack 최상위 연산자와 우선순위 비교
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