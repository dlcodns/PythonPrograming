import math

a, b, c = map(int, input().split())
answer = math.lcm(a, b, c)

print(answer)