# 과일 순회하며 번호 매기기
fruits = ["사과", "바나나", "체리"]

for i, fruit in enumerate(fruits):
    print(f'{i}. {fruit} ')
    
# start 파라미터 - 인덱스를 1부터 시작하기
for i, fruit in enumerate(fruits, start=1):
    print(f'{i}번째 과일: {fruit}')