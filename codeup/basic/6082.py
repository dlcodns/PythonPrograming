a = int(input())

for i in range(1, a+1):
    if i<=10:
        if i%3==0:
            print('X', end=' ')
        else:
            print(i, end=' ')
            
    else:
        second = i//10
        first = i%10
        
        if second%3==0 or first%3 ==0 and first!=0:
            print('X', end=' ')
        else:
            print(i, end=' ')