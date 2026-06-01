n = int(input())
stu = list(map(int, input().split()))
a = [0]*23

for s in stu:
    a[s-1]+=1
    
for b in a:
    print(b, end = ' ')