#팩토리얼 0의 개수
#N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 
# 0의 개수를 구하는 프로그램을 작성하시오.

N = int(input())
result = 1
count=0

for i in range(1,N+1):
    result *= i

while result%10==0:
    result = result//10
    count= count+1

print(count)