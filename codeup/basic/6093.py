n = int(input())
stu = list(map(int, input().split()))

list.reverse(stu)

for s in stu:
    print(s, end=' ')