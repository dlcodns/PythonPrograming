#최단경로

import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
K = int(input())

dp = [INF]*(V+1)
heap = []
graph = [[] for _ in range(V+1)]

def Dijkstra(start):
    #시작 정점은 0으로 초기화
    dp[start] = 0
    #힙큐에 초기화 가중치랑 정점을 넣음
    heapq.heappush(heap,(0,start))

    while heap:
        wei,now = heapq.heappop(heap)

        if dp[now] <wei:
            continue

        #now에 인접 점 확인
        for w, next_node in graph[now]:
            next_wei = w+wei

            #원래 최소 보다 작으면 바꾸기, 첫 dp는 INF
            if next_wei<dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(heap,(next_wei, next_node))

#노드와 엣지 받기
for _ in range(E):
    u, v, w = map(int,input().split())
    graph[u].append((w,v))

Dijkstra(K)
for i in range(1,V+1):
    print("INF" if dp[i] == INF else dp[i])