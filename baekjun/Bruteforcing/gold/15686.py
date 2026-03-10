# 치킨 배달
# 크기가 N×N인 도시가 있다. 
# 도시는 1×1크기의 칸으로 나누어져 있다. 
# 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나이다. 
# 도시의 칸은 (r, c)와 같은 형태로 나타내고, 
# r행 c열 또는 위에서부터 r번째 칸, 
# 왼쪽에서부터 c번째 칸을 의미한다. 
# r과 c는 1부터 시작한다.

# 이 도시에 사는 사람들은 치킨을 매우 좋아한다. 
# 따라서, 사람들은 "치킨 거리"라는 말을 주로 사용한다. 
# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. 
# 즉, 치킨 거리는 집을 기준으로 정해지며, 
# 각각의 집은 치킨 거리를 가지고 있다. 
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.

# 임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 
# |r1-r2| + |c1-c2|로 구한다.

# 예를 들어, 아래와 같은 지도를 갖는 도시를 살펴보자.
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 1
# 0 0 0 1 2
# 0은 빈 칸, 1은 집, 2는 치킨집이다.

# 이 도시에 있는 치킨집은 모두 같은 프랜차이즈이다. 
# 프렌차이즈 본사에서는 수익을 증가시키기 위해 
# 일부 치킨집을 폐업시키려고 한다. 오랜 연구 끝에 이 도시에서 
# 가장 수익을 많이 낼 수 있는  치킨집의 개수는 
# 최대 M개라는 사실을 알아내었다.

# 도시에 있는 치킨집 중에서 최대 M개를 고르고, 
# 나머지 치킨집은 모두 폐업시켜야 한다.
#  어떻게 고르면, 도시의 치킨 거리가 
# 가장 작게 될지 구하는 프로그램을 작성하시오.

import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
city = []
for _ in range(N):
    city.append(list(map(int, input().split())))

houses = []
chickens = []

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            houses.append((r, c))
        elif city[r][c] == 2:
            chickens.append((r, c))

result = float('inf')

for selected in combinations(chickens, M):
    total = 0
    for hr, hc in houses:
        min_dist = float('inf')
        for cr, cc in selected:
            min_dist = min(min_dist, abs(hr - cr) + abs(hc - cc))
        total += min_dist
    result = min(result, total)

print(result)