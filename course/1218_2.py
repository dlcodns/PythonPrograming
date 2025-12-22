# num=30
# if num > 30:
#     print("30보다 크다")
# else:
#     print("30보다 크지 않다")

# #str은 어떤 멤버를 가지고 있는지 출력해줘
# print(dir(str))

# #str에 있는 find라는 함수에 대해서 설명해줘
# help(str.find)
# print("Hello".find("o",2,5))
"""
print(0.2*1000)
print((1.0-0.8) == 0.2)
"""

#str은 부분적으로 변경하는 것이 안됨
"""
name = "adam"
name = "eve"
print(name)
print(name[0])
name = "a"
"""

#list
"""
names = ["adam", "eve", "jessica"]
print(names)
print(names[1])
names[2] = "hunt"
print(names)
"""

#tuple
"""
adam = ("singer", 38, "강남구 역삼동")
print(adam)
names[0] = "talent"
"""

#set
"""
dice={1,2,3,4,5,6,1}
print(dice)
"""

#dick
"""
adam = {"name":"adam","job":"singer","age":55, "job": "programmer"}
print(adam)
print(adam["job"])
"""

#제어
"""
print("Hello\n nward")
"""

#예약어
"""
import keyword
print(keyword.kwlist)

print(dir(str))
str = 500
print(dir(str))
"""

#연산자
"""
result = 10+20
print(result)

result = ["10","20"]*3
print(result)
"""

print(dir(slice))