import sys
from collections import deque


# 프린터
def solution(priorities, location):
    priorities = deque(priorities)
    count = 0

    while True:
        location -= 1

        max_value = max(priorities)
        check = priorities.popleft()
        
        if location == -1:
            if check < max_value:
                priorities.append(check)
                location = len(priorities)-1
            else:
                return count + 1
        elif check < max_value:
            priorities.append(check)
        else:
            count += 1

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, location = map(int, sys.stdin.readline().split())
        priorities = list(map(int, sys.stdin.readline().split()))
        print(solution(priorities, location))


    # print(solution([2, 1, 3, 2], 2))    # 1
    # print(solution([1, 1, 9, 1, 1, 1], 0))    # 5