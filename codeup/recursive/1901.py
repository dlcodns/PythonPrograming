def a(i, n):
    if i>n:
        return 0
    print(i)
    a(i+1,n)
    
n = int(input())

a(1, n)