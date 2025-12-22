"""
class 이름:
    속성
    메서드
"""
"""
class Address:
    def printAddress(self):
        print("인스턴스 메서드 만들기 연습")

    

#Address 클래스의 인스턴스 만들기
address = Address()

#바운드 호출: 인스턴스 이름으로 호출
address.printAddress()

#언바운드 호출: 클래스 이름으로 호출
Address.printAddress(address)
"""
"""
class Address:
    num = 0        
    

#Address 클래스의 인스턴스 만들기
address = Address()
print(Address.num)
print(address.num)
print("===========")
Address.num = 10
#클래스를 이용해서 수정
print(Address.num)
print(address.num)
print("===========")
address.num = 20
#인스턴스를 이용해서 수정: 인스턴스 안에 별도로 생성하고 클래스의 속성은 변경하지 않음
print(Address.num)
print(address.num)
print("===========")
print(id(address.num))
print(id(Address.num))
"""
"""
class Address:
    num = 0        
    def getNum():
        return num
    def setNum(num1):
        num= num1
    

#Address 클래스의 인스턴스 만들기

Address.setNum(10)
print(Address.getNum())
"""


class Address:
    auto_increment=1

    @staticmethod
    def method1(initValue):
        print("이 메서드로 하는 일은 일반적으로 static 변수의 초기화를 수행합니다.")
        Address.auto_increment = initValue

    def __init__(self,name, mobile="전화번호없음"):
        self.__id = Address.auto_increment
        self.__name = name
        self.__mobile = mobile
        
        Address.auto_increment = Address.auto_increment+1

    def __del__(self):
        print("메모리해제")


    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        print("name의 getter 호출")
        return self.__name

    @name.setter    
    def name(self,name):
        print("name의 setter 호출")
        if len(self.name) <= 5:
            print("이름이 너무 깁니다.")
            return
        self.__name = name

    @property
    def mobile(self):
        return self.__mobile
    
    @mobile.setter
    def setMobile(self,mobile):
        self.__mobile = mobile

    #+연산자 오버로딩
    def __add__(self, other):
        return self.name+other.name
    
    def __str__(self):
        return str(self.__id)


address1 = Address("박문석", "010320424")
address2 = Address("김근아", "0104")


print(address1)
print(address2)

class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.__instance = object.__new__(cls,*args, **kwargs)
            return cls.__instance
        
class Sub(Singleton):
    a=10

sub1 = Sub()
sub2 = Sub()
print(sub1 is sub2)



# address = Address(name = "이채운", mobile=" 010")

# #인스턴스를 통해서 속성을 접근하는 것처럼 보이지만 실제로는 접근자 
# address.name = "aaaadam"
# print(address.name)
# address = Address(name = "이채운", mobile=" 010")
# # address.setId(1)
# # address.setName("이채운")
# # address.setMobile("010")
# print(address.getId())
# address4 = address
# address=None
# #print(address.getId())

# address1 = Address(name = "ㅇㄴㄹ", mobile="321")
# # address1.setId(2)
# # address1.setName("이운")
# # address1.setMobile("111")
# print(address1.getId())


# address2 = Address(name = "가나디")

# print(address2.getId())
