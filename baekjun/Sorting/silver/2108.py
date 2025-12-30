#통계학

#수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 
# 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 
# 단, N은 홀수라고 가정하자.

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
num = []
avg = 0

for i in range(N):
    num.append(int(input()))

#산술평균
avg = sum(num)/N

num.sort()

#중앙값
middle = num[N//2]

#최빈값
#셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

#Counter(): key = 숫자, value = 등장 횟수
cnt = Counter(num)
#cnt의 values 중 가장 큰 값
max_freq = max(cnt.values())

#modes[]에 최빈값들 넣기
modes = [k for k, v in cnt.items() if v == max_freq]
#sort해서 최빈값이 여러개면 [1]번째 출력, 한 개면 [0] 출력
modes.sort()
most = modes[0] if len(modes) == 1 else modes[1]

#범위
rng = num[N-1]-num[0]

print(round(avg))
print(middle)
print(most)
print(rng)