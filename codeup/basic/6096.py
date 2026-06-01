d = [list(map(int, input().split())) for _ in range(19)]
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    
    for j in range(19):
        if d[a-1][j] == 0: d[a-1][j]=1
        else: d[a-1][j]=0
    for k in range(19):
        if d[k][b-1] == 0: d[k][b-1]=1
        else: d[k][b-1]=0
        
for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()