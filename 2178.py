import sys
from collections import deque


row, col = map(int, sys.stdin.readline().split())
matrix = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(row)]


def bfs(start):
    queue = deque([start])
    visited = [start]
    
    while queue:
        current_node = queue.popleft()
        for search_node in range(len(matrix)):
            if matrix[current_node][search_node] and search_node not in visited:
                visited.append(search_node)
                queue.append(search_node)
    return visited

print(bfs(0))

