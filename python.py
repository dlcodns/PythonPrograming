class Student:
    def __init__(self, name="noname"):
        self.__name = name
    
    def setName(self, name):
        print("setter 호출")
        self.__name = name

    def getName(self):
        print("getter 호출")
        return self.__name
    
    def __add__(self, other):
        return self.name+","+other.name
    
    def __str__(self):
        return self.__name+"2"
    
# stu1 = Student()
# stu1.name = "아담"

# stu2 = Student()
# stu2.name = "류시아"

# print(stu1+stu2)

stu = Student()
stu.name = "아담"
print(stu)