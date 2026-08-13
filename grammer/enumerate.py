# 과일 순회하며 번호 매기기: 0부터 셈
fruits = ["사과", "바나나", "체리"]

for i, fruit in enumerate(fruits):
    print(f'{i}. {fruit} ')
    
# start 파라미터 - 인덱스를 1부터 시작하기
for i, fruit in enumerate(fruits, start=1):
    print(f'{i}번째 과일: {fruit}')
    
# 특정 조건의 인덱스와 값만 찾기
numbers = [10, 25, 33, 47, 52, 61]

even_indices = [i for i, num in enumerate(numbers) if num % 2 ==0]
even_nums = [num for i, num in enumerate(numbers) if num%2==0]
print(even_indices)
print(even_nums)

for i, num in enumerate(numbers):
    if num%2==0:
        print(f'{i}: {num}')
    
# 리스트 값을 인덱스 기준으로 수정하기
scores = [80,90,75,60]
for i, score in enumerate(scores):
    if score<70:
        scores[i] = 0
print(scores)