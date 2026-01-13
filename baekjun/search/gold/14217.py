#그래프 탐색

#알고리즘 수업 - 너비 우선 탐색 1

import sys
from collections import deque

input = sys.stdin.readline

#첫째 줄: 도시의 개수 n, 도로의 개수 m
N, M = map(int, input().split())

#인접리스트
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

Q = int(input())


def bfs(start):
    visited = [False] * (N+1)
    queue = deque([start])
    visited[start] = True
    distance = [-1] * (N+1)
    distance[start] = 0
    
    while queue:
        node = queue.popleft()
        
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                distance[next_node] = distance[node]+1
                queue.append(next_node)
    
    for i in range(1, N+1):
        print(distance[i], end=" ")
    print()



for _ in range(Q):
    a, i, j = map(int, input().split())
    
    #a가 1일때는 두 도시 i,j를 잇는 도로를 만들고
    if a==1:
        graph[i].append(j)
        graph[j].append(i)

    #a가 2일때는 i,j를 잇는 도로를 없앤다
    else:
        graph[i].remove(j)
        graph[j].remove(i)

    bfs(1)