#대문자보다 소문자가 더 크다
"""
li1 = ["adam", "eve"]
li2 = ["Singer"]

print(li1>li2)
"""

#문자열(str)과 리스트에 ==와 !=를 사용할 수 있는지 확인해보기
"""
li1 = ["adam", "eve"]
li2 = "adam"

print(li1==li2)
print(li1!=li2)
"""

#없는 것을 찾으면 (-1) 2의 보수가 나옴
"""
print("Hello".find("e"))
print("Hello".find("k"))
"""

#3) 논리 비트 연산자
"""
print(True and False)
print(bool(10 and 0))
print(bool([] or [1,2,3]))
"""

#4) 기타 연산자 type, id
"""
a = 1
b = 2
print(id(a))
print(id(b))
"""

#입력받아서 정수로 변환 + if문
"""
score= int(input("점수를 입력하세요"))
print(score)

if score>=80 and score<=100:
    print("합격입니다!")
elif score>=60 and score <=79:
    print("보류입니다.")
elif score>=0 and score <=59:
    print("불합격입니다...")
else:
    print("잘못된 점수를 입력한 것 같습니다.")
"""

#match
"""
status = 404
status = int(input())
match status:
    case 404:
        print("잘못된 URL")
    case 200:
        print("OK")
    case _:
        print("etc")
"""

#while
"""
n=1
while n<= 10:
    print(n)
    n+=1
"""

#빨강 파랑 녹색을 번걸아 출력하기
"""
import time

while True:
    print("빨강")
    time.sleep(1)
    print("파랑")
    time.sleep(1)
    print("녹색")
    time.sleep(1)
"""
"""
import time
n=0
while True:
    if(n%3==0):
        print("빨강")
    if(n%3==1):
        print("파랑")
    if(n%3==2):
        print("녹색")
    n+=1
    time.sleep(1)
"""
"""
import time
n=0
while True:
    match n%3:
        case 0:
            print("빨강")
        case 1:
            print("파랑")
        case 2:
            print("녹색")
    n+=1
    time.sleep(1)
"""

#1~2025년까지 윤년의 개수 구하기
"""
year=1
count=0

while year<=2025:
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        count+=1
    year+=1

print(count)
"""

#else: 중간에 중단하지 않고 완료했을 때 수행
"""
n=1
while n < 11:
    print(n)
    n=n+1
else:
    print("완료")
"""

#2부터 1000까지 소수의 개수 구하기

"""미완
cnt =0

for i in range(2,1001):
    count=0
    for j in range(i,i+1):
        if i%j==0:
            count+=1
    if count==2:
        cnt+=1
print(cnt)
"""


#2부터 1000까지 완전수(자신을 제외한 약수의 합이 자신과 동일한 수) 구하기

"""
games = ["강진 축구", "프리스턴 테일", "아이온"]
for game in games:
    print(game)

for su in range(10):
    print(su)
"""
"""
games = ["강진 축구", "프리스턴 테일", "아이온"]
for game in games:
    if len(game) > 5:
        continue
    print(game)
else:
    print("반복문을 정상적으로 종료한 경우만 수행합니다.")
print("무조건 수행합니다.")
"""

#이거 만들어보기

"""

    *
  * * *
* * * * *
  * * *
    *

          0
        1 0 2
      3 0 0 0 4
    5 0 0 0 0 0 6
  7 0 0 0 0 0 0 0 8
9 0 1 2 3 4 5 6 7 8 9



"""
"""
def sub(first:int, second:int=0):
    result = first-second
    return result

print(sub(100,200))
print(sub(first=100, second=200))
print(sub(first=200))
"""
"""
def sub(first:int, second:int) -> int:
    result = first-second
    return result
print(sub(first=100, second = 70))
print(sub(*[100,70]))

print(sub(first=100, second=70))
print(sub(*[100,70]))
"""
"""
def tot(*arg):
    result = 0
    for x in arg:
        result = result+x
    return result

print(tot(10,20))
print(tot(10,20,30))
print(tot(10,20,30,40))
"""
"""
def fibonacci1(su: int)-> int:
    result = 1
    first = 1
    second = 1
    for _ in range(3,su+1,1):
        result = first+second
        second = first
        first = result
    return result

def fibonacci2(su:int)->int:
    if su==1 or su==2:
        return 1
    else:
        return fibonacci2(su-1)+fibonacci2(su-2)

print(fibonacci1(10))
print(fibonacci2(100))
"""

def deco(func):
    def inner():
        print("실제 수행할 함수")
    return inner


@deco
def target():
    print("running target")

#target 함수 위에 deco 추가했기 때문에 deco가 리턴하는 함수를 호출
target()