# def de(a, b):
#     if a%2!=0 and a+2<=b:
#         print(a, end=' ')
#         de(a+2, b)
#     elif a%2!=0:
#         print(a, end=' ')
#     elif a%2==0 and a+1<=b:
#         de(a+1,b)
#     else:
#         return 0
        
    
# a, b = map(int, input().split())
# de(a, b)

def de(a,b):
    if a>b: return
    if a%2!=0:
        print(a, end = ' ')
    de(a+1,b)
        
a, b = map(int,input().split())
de(a,b)