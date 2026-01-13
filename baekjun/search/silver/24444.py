#알고리즘 수업 - 너비 우선 탐색 1

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

visited = [0] * (N+1)

def bfs(start):
    queue = deque([start])
    visited[start] = 1
    order = 1
    result = [0] * (N+1)
    result[start] = order
    
    while queue:
        node = queue.popleft()
        
        for next_node in graph[node]:
            if visited[next_node] == 0:
                order += 1
                visited[next_node] = 1
                result[next_node] = order
                queue.append(next_node)
    
    for i in range(1, N+1):
        print(result[i])

bfs(R)