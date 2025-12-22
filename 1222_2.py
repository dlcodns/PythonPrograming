class Super:
    def __init__(self, name):
        print("Super의 init")

    def greeting(self):
        print("상위 클래스의 메서드")


#Super 클래스의 모든 것을 상속 받습니다.
class Sub(Super):
    #상위 클래스에 __init__에 매개변수를 대입해야 하는 경우에는
    #하위 클래스에 __init__을 만들어서 super().__init__을 명시적으로 호출해야 합니다.
    def __init__(self):
        super().__init__("이채운")
    
    #메서드 오버라이딩
    def greeting(self):
        super().greeting()
        print("하위 클래스의 메서드")


sub = Sub()
sub.greeting()