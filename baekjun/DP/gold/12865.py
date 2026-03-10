# 평범한 배낭

import sys
input = sys.stdin.readline

N, K = map(int,input().split())

item = [[0]*2 for i in range(N)]

for i in range(N):
    W, V = map(int, input().split())
    item[i][0] = W
    item[i][1] = V

dp = [0]*(K+1)

for i in range(N):
    w,v = item[i][0], item[i][1]
    for j in range(K, w-1, -1):
        dp[j] = max(dp[j], dp[j-w] + v)

answer = dp[K]
print(answer)