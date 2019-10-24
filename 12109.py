import sys


def solution(citations):
    answer = 0
    citations = list(map(int, citations))
    citations.sort()
    h = len(citations)
    for i in range(h):
        if citations[i] >= h-i:
            return h - i
    return answer

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    citations = list(sys.stdin.readline().split())
    print(solution(citations))