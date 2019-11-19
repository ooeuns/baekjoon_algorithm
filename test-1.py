import sys
import collections

def in_board(yx):
    x, y = yx
    return 1 <= x and x <= row - size_y + 1 and 1 <= y and y <= col - size_x + 1

# s, e is a tuple
def find_min_route(start, end):
    queue = collections.deque([(start,0)])
    while queue:
        cur_pos, cur_step = queue.popleft()
        if cur_pos in visit:
            continue

        visit.add(cur_pos)    

        if cur_pos == end:
            return cur_step

        around = [(cur_pos[0]+dy, cur_pos[1]+dx) for dy, dx in d]
        for cs in around:
            if cs == end:
                return cur_step+1
            if cs not in visit and in_board(cs) and cs not in break_points:
                queue.append([cs, cur_step+1])

    return -1

row, col, size_y, size_x, K = map(int, sys.stdin.readline().split())
d = [(-1,0), (1,0), (0,-1), (0,1)]
break_points = set()
visit = set()


for _ in range(K):
    bx, by = map(int, sys.stdin.readline().split())
    break_points.update([(bx-dx, by-dy) for dx in range(0, size_y) for dy in range(0, size_x)])


start = tuple(map(int, sys.stdin.readline().split()))
end = tuple(map(int, sys.stdin.readline().split()))

print(find_min_route(start, end))
