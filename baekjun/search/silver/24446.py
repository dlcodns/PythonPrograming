#알고리즘 수업 - 너비 우선 탐색 3

import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())

#인접리스트
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

visited = [False] * (N+1)
depth = [-1] * (N+1)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    depth[start] = 0
    
    while queue:
        node = queue.popleft()
        
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                depth[next_node] = depth[node]+1
                queue.append(next_node)
    
    for i in range(1, N+1):
        print(depth[i])

bfs(R)