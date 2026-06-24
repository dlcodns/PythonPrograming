item, money = map(int, input().split())

coin = dict()
coin[500] = 0
coin[100] = 0
coin[50] = 0
coin[10] = 0

N = money-item

if N >= 500:
    coin[500] = N//500
    N = N%500
if N>=100:
    coin[100] = N//100
    N = N%100
if N>=50:
    coin[50] = N//50
    N = N%50
if N>=10:
    coin[10] = N//10

print(sum(coin.values()))