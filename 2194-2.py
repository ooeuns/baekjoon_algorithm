from collections import deque
import sys


def check_bounds(yx):
    y, x = yx
    return (1 <= y <= (row - size_y + 1)) and (1 <= x <= (col - size_x + 1))
    

def game(start, end):
    queue = deque([[start[0], start[1], 0]])
    while queue:
        y, x, dist = queue.popleft()
        if (y, x) in visited:
            continue
        visited.add((y, x))

        around = [(y+dy, x+dx) for dy, dx in AROUND]
        for cs in around:
            if cs == end:
                return dist+1

            if cs not in visited and cs not in obstacles and check_bounds(cs):
                queue.append([cs[0], cs[1], dist+1])
    return -1


if __name__ == "__main__":
    # initialization
    AROUND = ((-1, 0), (0, 1), (1, 0), (0, -1))

    # create map
    row, col, size_y, size_x, K = map(int, sys.stdin.readline().split())

    obstacles = set()
    visited = set()

    # create obstacle
    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split())
        obstacles.update([(y-dy, x-dx) for dy in range(size_y) for dx in range(size_x)])
        
    # start, end points
    start = tuple(map(int, sys.stdin.readline().split()))
    end = tuple(map(int, sys.stdin.readline().split()))

    print(game(start, end))
