import sys
input=sys.stdin.readline

def check(num):
    for x in str(i):
        if x in broken:
            return False
    return True

n=int(input())
m=int(input())
broken=list(map(str,input().split()))
result=abs(n-100)

for i in range(1000000): #0~999,999
    if check(i):
        result=min(len(str(i))+abs(i-n) , result)

print(result)
    



    
    
    


