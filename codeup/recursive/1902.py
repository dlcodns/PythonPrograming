def a(n,i):
    if n<i:
        return 0
    print(n)
    a(n-1, 1)
    
n = int(input())
a(n,1)