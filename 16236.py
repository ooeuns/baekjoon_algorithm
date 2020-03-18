import sys
from collections import deque

AROUND = ((-1, 0), (1, 0), (0, -1), (0, 1))


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
    if not find_little_fish(shark[2]):
        return shark[3]

    while True:

        fishes = []
        while queue:
            y, x, size, dist = queue.popleft()

            for dy, dx in AROUND:
                mv_y, mv_x = y+dy, x+dx
                if in_boundary((y, x)) and ocean[mv_y][mv_x] <= size:
                    queue.append((mv_y, mv_x, size, dist+1))

                    if ocean[mv_y][mv_x] and ocean[mv_y][mv_x] < size:
                        fishes.append((mv_y, mv_x, size+1, dist+1))

            if len(fishes) == 0:
                continue
            elif len(fishes) == 1:
                queue = deque([fishes.pop()])
                break
            else:
                fishes.sort(key=lambda x: (x[0], x[1]))
                next_pos = fishes.pop()
                ocean[next_pos[0]][next_pos[1]] = 0
                queue = deque([next_pos])
                break

    return


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
