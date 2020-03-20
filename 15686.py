import sys
import heapq


def solution(M: int):
    heap = []
    for s in store:
        dist = 0
        for h in house:
            dist += abs(h[0] - s[0]) + abs(h[1] - s[1])
        heapq.heappush(heap, dist)
    print(heap)
    return sum(heap[:M])


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    city = [[0]*(N+1) for _ in range(N+1)]

    house = []
    store = []

    for row in range(1, N+1):
        tmp = list(map(int, sys.stdin.readline().split()))

        for col in range(1, N+1):
            city[row][col] = tmp[col-1]
            if tmp[col-1] == 1:
                house.append((row, col))
            elif tmp[col-1] == 2:
                store.append((row, col))
    print(solution(M))
