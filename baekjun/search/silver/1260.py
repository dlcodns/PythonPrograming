#DFS와 BFS

import sys
from collections import deque

input = sys.stdin.readline
#N: 정점의 개수, M: 간선의 개수, V: 탐색 시작 정점
N, M, V = map(int, input().split())

#양방향 간선을 2차원 배열로 표현(N+1 정사각 행렬)
graph = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited1 = [0]*(N+1)
visited2 = visited1.copy()


def dfs(V):
    #[V] 탐색 시작 => 1로 변경
    visited1[V] = 1
    print(V, end=' ')

    for i in range(1, N+1):
        #만약 간선도 있고 방문 안 한 곳이라면 더 깊이 들어가기
        #1~ 순서대로 가서 작은 것부터 알아서 탐색됨
        if graph[V][i] == 1 and visited1[i] == 0:
            dfs(i)

def bfs(V):
    #bfs는 queue 사용, 탐색할 노드 삽입
    queue = [V]
    #[v] 탐색 시작해서 1로 변경 
    visited2[V] = 1

    #queue가 다 빠질 때까지, 처음에는 [V] 상태임
    while queue:
        #첫번째 노드를 뺌
        V = queue.pop(0)
        print(V, end = ' ')

        for i in range(1, N+1):
            #만약 i(도착지)가 간선이 있고, 방문 안했다면 
            #i를 큐에 넣고 방문 체크
            if(graph[V][i] == 1 and visited2[i] == 0):
                queue.append(i)
                visited2[i]=1

dfs(V)
print()
bfs(V)