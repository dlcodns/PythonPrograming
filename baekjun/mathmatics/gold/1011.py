#Fly me to the Alpha Centauri

# import sys

# input = sys.stdin.readline

# T = int(input())

# def fly(count, gap, K):
#     print("\n", K, "\n")
#     #기본적인 상황
#     if gap == (K+1):
#         gap = gap-(K+1)
#         count+=1
#         return count
    
#     elif gap == K:
#         gap = gap-K
#         count+=1
#         return count
    
#     elif gap == (K-1):
#         gap = gap-(K-1)
#         count+=1
#         return count

#     #특이 사항
#     else:
#         gap = gap-(K+1)
#         count+=1
#         fly(count, gap, K)

# for _ in range(T):
#     X, Y = map(int, input().split())
#     count = 2

#     gap = Y-X-2
#     K=1

#     count = fly(count, gap, K)

#     print(count)

import sys
import math

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    d = y - x

    k = int(math.isqrt(d))

    if d == k * k:
        print(2 * k - 1)
    elif d <= k * k + k:
        print(2 * k)
    else:
        print(2 * k + 1)
