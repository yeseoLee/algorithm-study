from sys import stdin

def getArea(a,b,c):
    area=10
    return area

n=int(stdin.readline())
dot=[[0]*2 for i in range(n)]
for i in dot:
    i[0],i[1]=map(int,stdin.readline().split())

"""
(n-2)개의 삼각형 결정 => 각 삼각형 넒이들의 합
재귀함수?  n각형 넓이 = 하나의 삼각형 넓이+(n-1)각형의 넓이
도형이 두개로 분리 될 수도...
오목다각형이나 볼록다각형은 아무 점이나 잡아선 안된다.
n점이라고 꼭 n각형일 필요는 없다( 3점이 일직선상에 존재)
1.임의의 두점에서 가장 가까운 한점 선택(x)
2.가장 좁은 각을 이루는 세 점(x)
3.보조선(x)
4. 삼각형 한개와 (n-1)각형 한개로 분리시켜주는 선을 찾아라

두점을 잇는 직선이 다각형 내부에 있냐?
나중에 이어풀자


"""
