#클래스 선언
class Calc:
    #생성자
    def __init__(self,first,second):
        self.first=first
        self.second=second
    #메서드
    def setdata(self, first, second):
        self.first=first
        self.second=second
    def add(self):
        return self.first + self.second
    def mul(self):
        return self.first * self.second
    def sub(self):
        return self.first - self.second
    def div(self):
        return self.first / self.second

#상속
class ExtendCalc(Calc):
    def pow(self):
        return self.first ** self.second 

#메서드 오버라이딩
class SafeCalc(Calc):
    def div(self):
        if(self.second): return self.first/self.second
        else: return "(0으로 나눌 수 없음)"

#클래스 변수
class Family:
    lastname = "김"

#출력
a=Calc(4,2)
print(f"{a.first}+{a.second} = {a.add()}")
a.setdata(5,4)
print(f"{a.first}-{a.second} = {a.sub()}")

b=ExtendCalc(4,2)
print(f"{b.first}+{b.second} = {b.add()}")
print(f"{b.first}^{b.second}={b.pow()}")

c=SafeCalc(3,0)
print(f"{c.first}/{c.second} = {c.div()}")

d=Family()
e=Family()
print(d.lastname,e.lastname)
Family.lastname ="박"
print(d.lastname,e.lastname)
print(id(Family.lastname),id(d.lastname),id(e.lastname))
