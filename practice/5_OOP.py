"""
Class

"""

# #Student Class를 생성하고 인스턴스를 만들고 Method를 사용
# class Student:
#     def insa(self):
#         print("안녕하세요")

#     def printName(self, name):
#         self.insa()
#         print("내 이름은", name)

# stu = Student()
# #바운드 호출
# stu.printName("사이버가수 아담")
# #언바운드 호출
# Student.printName(stu, "군계")



# #self
# import time

# class Student:
#     #생성자
#     def __init__(self, name = "사이버가수"):
#         print(time.ctime(),"에 인스턴스가 생성되었습니다.")
#         self.name = name

#     def setName(self, name):
#         self.name = name

#     def getName(self):
#         return self.name
    
# student = Student()
# student.setName("아담")
# print(student.getName())


#Attribute
# class Student:
#     schoolName = "Korea"


# stu1 = Student()
# stu2 = Student()

# print("stu1의 참조:", id(stu1))
# print("stu2의 참조:", id(stu2))
# print("=====================")

# print("Student의 학교:", Student.schoolName)
# print("stu1의 학교:", stu1.schoolName)
# print("stu2의 학교:", stu2.schoolName)
# print("=====================")

# #class를 이용해서 attribute를 변경하면 전부 변경됨
# Student.schoolName = "Seoul"
# print("Student의 학교:", Student.schoolName)
# print("stu1의 학교:", stu1.schoolName)
# print("stu2의 학교:", stu2.schoolName)
# print("=====================")

# #인스턴스 이용해서 하면 그 인스턴스만 변경됨
# stu1.schoolName = "KAIST"
# print("Student의 학교:", Student.schoolName)
# print("stu1의 학교:", stu1.schoolName)
# print("stu2의 학교:", stu2.schoolName)
# print("\n")



#==: 데이터를 비교하기 위한 연산자 [a==b] = [a.__eq__(b)]
#is: id 값의 일치 여부를 확인하는 연산자. 오버로딩 불가능



#Accessor
#Getter: Attribute의 값을 리턴해주는 Method, 타입이 bool일 경우, get 대신 is 사용
#Setter: Attribute의 값을 설정해주는 Method

#Accessor 생성과 호출
# class Student:
#     def getName(self):
#         return self.name
    
#     def setName(self, name):
#         self.name = name

# student1 = Student()
# student1.setName("아담")

# student2 = Student()
# student2.setName("류시아")

# print(student1.getName())
# print(student2.getName())



#생성자와 소멸자
#가비지 컬렉션
##파이썬에서는 특별히 사용자가 메모리 관리 할 필요 없음
##메모리는 자동으로 할당되고 자동으로 해제
##모든 데이터는 참조 횟수를 가지고 있고 이 값이 0이 되면 자동으로 해제
# import time

# class Student:
#     def __init__(self, name="사이버가수"):
#         print(time.ctime(),"에 인스턴스가 생성되었습니다.")
#         self.name= name

#     def getName(self):
#         return self.name

#     def setName(self,name):
#         self.name = name

#     def __del__(self):
#         print(time.ctime(),"에 인스턴스가 소멸되었습니다.")

# stu1 = Student()
# stu1.setName("아담")
# print(stu1.getName())

# stu2 = Student()
# print(stu2.getName())

# #객체 소멸은 None을 대입해서 retain count를 1 감소시켜서 0으로 만들어서 삭제
# student1 = None
# student2 = None



#static method와 clas method
class Student:
    @classmethod
    def cmethod(cls):
        print("Class Method")
        print(cls)

    @staticmethod
    def smethod():
        print("정적 Method")

#클래스를 이용한 Method
Student.cmethod()
Student.smethod()

#인스턴스를 이용한 Method
student = Student
student.cmethod()
student.smethod()