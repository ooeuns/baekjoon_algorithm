import sys
from collections import deque

AROUND = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 0


def mv_shark(shark: tuple, next_pos: tuple):
    global cnt

    ocean[shark[0]][shark[1]] = 0
    ocean[next_pos[0]][next_pos[1]] = float('inf')

    cnt += 1
    if cnt == next_pos[2]:
        cnt = 0
        return (next_pos[0], next_pos[1], next_pos[2]+1, next_pos[3])

    return tuple(next_pos)


def find_little_fish(size: tuple):
    for o in ocean:
        for fish in o:
            if fish and fish < size:
                return True
    return False


def in_boundary(cur_pos):
    y, x = cur_pos
    if (y >= 0 and y < N) and (x >= 0 and x < N):
        return True
    return False


def solution(queue: list, ocean: list, shark: tuple):
    while True:
        if not find_little_fish(shark[2]):
            return shark[3]

        fishes = []
        visited = [[0]*N for _ in range(N)]
        while queue:
            y, x, size, dist = queue.popleft()

            for dy, dx in AROUND:
                mv_y, mv_x = y+dy, x+dx
                s = (mv_y, mv_x, size, dist+1)
                if in_boundary((mv_y, mv_x)):
                    if not visited[mv_y][mv_x] and ocean[mv_y][mv_x] <= size:
                        visited[mv_y][mv_x] = 1
                        queue.append(s)
                        if ocean[mv_y][mv_x] and ocean[mv_y][mv_x] < size:
                            fishes.append(s)

            if len(queue) == 0:
                return shark[3]

            if queue[0][3] == dist:
                continue

            if len(fishes) == 0:
                continue
            elif len(fishes) == 1:
                next_pos = mv_shark(shark, fishes[0])
                shark = next_pos[:]
                queue = deque([next_pos])
                break
            else:
                fishes.sort(key=lambda x: (x[0], x[1]))
                next_pos = mv_shark(shark, fishes[0])
                shark = next_pos[:]
                queue = deque([next_pos])
                break


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    shark = tuple()
    ocean = []

    for idx in range(N):
        lst = list(map(int, sys.stdin.readline().split()))
        if 9 in lst:
            shark = (idx, lst.index(9), 2, 0)
        ocean.append(lst)

    print(solution(deque([shark]), ocean, shark))
