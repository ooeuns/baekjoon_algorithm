import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
# ocean = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 1],
#     [0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0]
# ]


ocean = [[0] * (N + 1) for _ in range(N + 1)]
for idx in range(1, N+1):
    link = list(map(int, sys.stdin.readline().split()))
    for i, li in enumerate(link):
        if li:
            ocean[idx][i+1] = 1
            ocean[i+1][idx] = 1

dist = [0] * (N + 1)

def dfs(start):
    visited = [start]
    queue = deque([start])
    dist[start] = 1
    
    while queue:
        current_node = queue.popleft()
        ans = []
        for search_node in range(len(ocean[current_node])):
            if ocean[current_node][search_node] and not search_node in visited:
                queue.append(search_node)
                visited.append(search_node)
                dist[search_node] += dist[current_node] + 1
        
    for i in range(1, N+1):
        ans = []
        for j in range(1, N+1):
            if dist[j] == i:
                ans.append(j)
        if ans:       
            print(*ans)
    

if __name__ == "__main__":
    dfs(M)
