item, money = map(int, input().split())

N = money - item
count = 0

for c in (500, 100, 50, 10):
    count += N//c
    N %= c

print(count)