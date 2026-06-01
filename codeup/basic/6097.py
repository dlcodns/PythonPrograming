h, w = map(int, input().split())
dou =[[0]*w for _ in range(h)]

n = int(input())

for i in range(n):
    l, d, x, y = map(int,input().split())
    x -= 1
    y -= 1
    
    if d==0:
        for j in range(y, y+l):
            dou[x][j]=1
    else: 
        for j in range(x, x+l):
            dou[j][y]=1
            
for i in range(h):
    for j in range(w):
        print(dou[i][j], end = ' ')
    print()
