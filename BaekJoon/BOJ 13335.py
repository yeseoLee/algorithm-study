'''
다리의 길이는 w 단위길이(unit distance)이며,
각 트럭들은 하나의 단위시간(unit time)에 하나의 단위길이만큼만 이동할 수 있다고 가정한다.
동시에 다리 위에 올라가 있는 트럭들의 무게의 합은다리의 최대하중인 L보다 작거나 같아야 한다.
참고로, 다리 위에 완전히 올라가지 못한 트럭의 무게는
다리 위의 트럭들의 무게의 합을 계산할 때 포함하지 않는다고 가정한다.

'''
import sys
from collections import deque
n,w,l=map(int,sys.stdin.readline().split()) #트럭의 수, 다리길이, 최대하중
truck=list(map(int,sys.stdin.readline().split()))
time=0 #마지막 차가 들어가기 전까지의 시간만 구하면 된다. 이후 + w
dq=deque()
for i in truck:
    while(sum(dq)+i>l):
        dq.pop()
        if(len(dq)==0):
            time+=w-1
    dq.appendleft(i)
    time+=1
time+=w

print(time)
    
    
    
