from collections import deque

BACKSPACE = "-"
RIGHT = ">"
LEFT = "<"

def solution(password):
    # initialiization
    queue = deque(password)
    stack_1 = []
    stack_2 = []
    
    # running
    while queue:
        key_board = queue.popleft()
        if key_board == LEFT:
            if not stack_1:
                continue
            else:
                stack_2.append(stack_1.pop())
        elif key_board == RIGHT:
            if not stack_2:
                continue
            else:
                stack_1.append(stack_2.pop())
        elif key_board == BACKSPACE:
            if not stack_1:
                continue
            else:
                stack_1.pop()
        else:
            stack_1.append(key_board)

    while stack_2:
        stack_1.append(stack_2.pop())

    return ''.join(stack_1)

if __name__ == "__main__":
    # input
    N = int(input())
    passwords = [list(input()) for _ in range(N)]
    for password in passwords:
        print(solution(password))

    # print(solution("<<BP<A>>Cd-"))
    # print(solution("ThIsIsS3Cr3t"))
    # print(solution("f<->--><-l>>d---u-j><>-<u->xb<<axkh<-wk>k>--t--s<b<i<ir>--ey>t>>sx<-yb<>jw<-qaruwy<osnshf><<<-uzz--<"))
    # print(solution("f<->--><-l>>d---u-j><>-<u->xb<<a"))
