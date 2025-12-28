"""
class 클래스이름:
    내용

class 클래스이름(상위 클래스 나열):
    내용
"""
"""
class Super1:
    def method1(self):
        print("Super1의 Method")

class Sub(Super1):
    pass

sub = Sub()
sub.method1()
"""

"""
#다중상속
class Super1:
    def method(self):
        print("Super1의 Method")

class Super2:
    def method(self):
        print("Super2의 Method")


class Sub(Super1, Super2):
    pass

sub = Sub()
sub.method()
print(Sub.mro())
"""


#추상 클래스 만드는 방법 - 인스턴스는 생성 불가
# import abc

# class Super(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def method(self):
#         pass

# class Sub(Super):
#     def method(self):
#         print("추상 메서드 구현")

# sub = Sub()


"""
import abc

class Login(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def login(self, id, pw):
        pass

class LoginImpl(Login):
    def login(self,id,pw):
        print("id와 pw를 가지고 로그인을 수행합니다.")

user = LoginImpl()
user.login("adam","1234")
"""

"""
import abc

class Star(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def attack(self):
        pass

class Terran(Star):
    def attack(self):
        print("테란의 공격")

class Zerg:
    def attack(self):
        print("저그의 공격")

class Protoss:
    def attack(self):
        print("프로토스의 공격")


star = Terran()
star.attack()
star = Zerg()
star.attack()
star = Protoss()
star.attack()
"""

"""
import sys
for p in sys.path:
    print(p)
"""

"""
class Person:
    def __init__(self):
        self.name = ""
        self.age = 0

    __slots__ = ["name", "age"]

#데이터를 만드는 부분
person1 = Person()
person1.name = "아담"
person1.age = 25

person2 = {"name":"류시아", "age":22}
person2["location"]="daejeon"

#데이터를 출력하는 부분
print("이름:", person1.name, "\n나이:", person1.age)

for key in person2:
    print(key, ":", person2[key])

"""

"""
me=["이채운", "대전", 25]
chung=["이충현", "대전", 26]
every=["dsa","123"]

#2차원 배열로 작성
couple = [me, chung]

#데이터가 추가되면 출력되는 부분을 수정
couple.append(every)

for i in range(len(couple)):
    if i == 0:
        print("채운: ", end="\t")
    elif i == 1:
        print("충현: ", end="\t")
    else:
        print("모두: ", end="\t")

    for info in couple[i]:
        print(info, end=" ")
    print()


all=[
    {"name":"채운", "information":me},
    {"name":"충현", "information":chung},
    {"name":"모두", "information":every},
]

for a in all:
    print(a["name"],":", end="\t")
    for information in a["information"]:
        print(information, end="\t")
    print()
"""

"""
data = [23, 25, 76, 19, 32]

#일반적인 방식
result = []
for i in data:
    result.append(i*2)

print(result)

#Comprehension 사용
result = [i*2 for i in data if i>30]
print(result)
"""

"""
from collections import Counter

counter = Counter(["red", "blue", "green", "red","red", "blue", "green", "red"])
print(counter)
print(counter["red"])
"""

"""
from collections import Counter

portfolio = [
    {"GOOG", 100, 490.1},
    {"IBM", 50, 91.1},
    {"CAT", 150, 83.44},
    {"GOOG", 120, 190.1},
    {"AAPL", 800, 190.1},
]

total_shares = Counter()
for name, shares, price in portfolio:
    total_shares[name] = total_shares[name]+1

print(total_shares)

total_shares = Counter()
for name,shares, price in portfolio:
    total_shares[name] = total_shares[name]+price
print(total_shares)

print(total_shares.most_common(3))
"""

"""
def ten_div(x:int) -> float:
    try:
        #예외가 발생하면 except 절로 이동해서 처리
        return 10/x
    except IndexError:
        return 100
    #0으로 나누는 경우에 발생하는 예외만 처리    
    except ZeroDivisionError:
        return 0

print(ten_div(2))
print(ten_div(0))
print(ten_div(5))
"""

"""
li = [100, 200, 300]

try:
    print(li[4])
except Exception:
    print("나머지 예외 처리")

#예외가 발생했을 때 예외 내용을 e에 전달
except IndexError as e:
    print(e)
else: 
    print("예외가 발생하지 않았을 때 처리")
finally:
    print("예외 발생 여부에 상관없이 처리")
"""

"""
x=199

assert x<50, "강제로 프로그램을 중단- Assertion"
"""

"""
try:
    #파일을 기록할 수 있도록 open
    file = open('./test.txt', 'w')
    #파일을 한 번에 기록
    file.write("Hello Python")
    file.write("\n\n")
    #줄바꿈이 있는 문자열을 줄 단위로 기록
    msg = "Hello\nPython"
    file.write("\n\n")
    file.writelines(msg)
    file.write(''.join(msg))

except Exception as e:
    print("파일 처리 중 예외 발생", e)
finally:
    file.close()
"""

#문자열을 분할해서 문자열 list 만들기
msg = "123 345 765 12"
result = msg.split(" ")
print(result)

print(result[0] + result[1])
print(int(result[0])+int(result[1]))