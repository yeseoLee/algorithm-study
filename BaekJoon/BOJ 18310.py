from sys import stdin
n=int(stdin.readline())
house=list(map(int,stdin.readline().split()))
house=sorted(house)
median=(n+1)//2
print(house[median-1])

'''
from sys import stdin

def binary():
    #거리의 합
    def dis(x):
        dis_sum=0
        for i in house:
            dis_sum+=abs(x-i)
        return dis_sum
    
    #초기화
    l,r=0,max(house)
    Ld,Rd=dis(l),dis(r)
    min_idx=l if Ld<=Rd else r
    min_dis=dis(min_idx)
    
    #이진탐색
    while(l<=r):
        mid=(l+r)//2
        Md=dis(mid)
        if(Md<min_dis or (Md==min_dis and mid<min_idx)):
            min_idx=mid
            min_dis=Md

        if(Ld<=Rd):
            r=mid-1
            Rd=dis(r)
        else:
            l=mid+1
            Ld=dis(l)
    return min_idx

n=int(stdin.readline())
house=list(map(int,stdin.readline().split()))
print(binary())
'''
