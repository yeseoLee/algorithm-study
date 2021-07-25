a,b=map(int,input().split())

def a_from_b(a,b):
    cnt=0
    while(b):
        cnt+=1
        if(b==a):
            return cnt
        if b%10==1 :
            b=b//10
            #return 1+a_from_b(a,b//10)
        elif b%2==0:
            b=b//2
            #return 1+a_from_b(a,b//2)
        else: #b%2!=0 and b%10!=1
            return -1
    return -1

print(a_from_b(a,b))
