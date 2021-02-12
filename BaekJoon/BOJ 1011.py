t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    cnt=0
    d=y-x
    k=1
    while(d>0):
        if(d>k):
            d-=k*2
            cnt+=2
        else:
            d-=k
            cnt+=1
        k+=1
    print(cnt)
'''
t=int(input()) #Test Case

for i in range(t):
    x,y = map(int, input().split())
    d=y-x #distance
    k=1;
    cnt=0;
    while(d>0):
        cnt+=1
        d-=k;
        if(cnt%2==0):
            k+=1
    print(cnt)
'''
