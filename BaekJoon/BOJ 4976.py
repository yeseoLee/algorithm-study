cnt=1
while(1):
    l,p,v=map(int,input().split())
    if(l+p+v==0):
        break
    day=(v//p)*l
    day+=min(v%p,l)
    print(f"Case {cnt}: {day}")
    cnt+=1
'''
연속하는 P일중 L일 동안만 사용할 수 있다.
V일짜리 휴가동안 최대 몇일 사용할 수 있는가?
=> V일 크기의 구간에서 P일 크기의 어느 구간을 잘라도 L일 이하이다.
OOOOOXXXOOOOOXXXOOOO
'''
