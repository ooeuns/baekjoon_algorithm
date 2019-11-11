import sys
import math
import collections

n, m, a, b, k = (map(int, sys.stdin.readline().split()))
d = [(-1,0), (1,0), (0,-1), (0,1)]
break_points = set()
visited = []
cached = {}

def in_board(p):
    x, y = p
    return 1 <= x and x <= n - a + 1 and 1 <= y and y <= m - b + 1

# s, e is a tuple
def find_min_route(s, e, history = [], depth = 0):
    queue = collections.deque()
    visit = set()
    queue.append((s,0))
    while queue:
        cur_pos, cur_step = queue.popleft()
        if cur_pos in visit:
            continue
        # print(f'cur : {cur_pos} cur step : {cur_step}')
        visit.add(cur_pos)       
        if cur_pos == e:
            return cur_step
        nest = [(cur_pos[0] +dx, cur_pos[1] + dy) for dx, dy in d]
        possible_nest = [(cs, cur_step+1) for cs in nest if cs not in visit and in_board(cs) and cs not in break_points]
        # print(possible_nest)
        queue.extend(possible_nest)
    return -1

for _ in range(k):
    bx, by = map(int, sys.stdin.readline().split())
    break_points.update([(bx-dx, by-dy) for dx in range(0, a) for dy in range(0, b)])

# print(break_points)

fs = tuple(map(int, sys.stdin.readline().split()))
e = tuple(map(int, sys.stdin.readline().split()))

min_route = find_min_route(fs, e)
if min_route == math.inf:
    print("-1")
else:
    print(str(min_route))