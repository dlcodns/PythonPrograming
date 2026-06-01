d = [list(map(int, input().split())) for _ in range(10)]
x=1
y=1

while True:
    if d[x][y] == 2:
        d[x][y]=9
        break
    
    d[x][y]=9
    
    if y+1<10 and d[x][y+1] != 1:
        y+=1    
    elif  x+1<10 and d[x+1][y] != 1:
        x+=1
    else:
        break
    


for i in range(10):
    for j in range(10):
        print(d[i][j], end = ' ')
    print()