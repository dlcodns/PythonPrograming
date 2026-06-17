# 거짓말
# 만약 "진실을 아는 사람의 수(T)" = 0 이면 answer = M
# OK
# 진실을 아는 사람이 파티에 있는 다른 사람에게 말할 수 있다.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li = list(map(int, input().split()))

if li[0] == 0:
    for _ in range(M):
        input()
    print(M)
    exit()

peo = li[0]
li = li[1:]



truth = [0]*N

for i in range(M):
    people = list(map(int, input().split()))
    truth[people[0]] = 1
    people = people[1:]
    
    for p in people:



