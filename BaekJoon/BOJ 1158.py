import sys
input=sys.stdin.readline

n,k=map(int,input().split())

result=[]
circle=[n for n in range(1,n+1)]
target=0

for i in range(n):
    target=(target+k-1)%(n-i)
    result.append(circle[target])
    del circle[target]
        
print("<" + ", ".join(map(str,result)) + ">")

'''
import sys
input=sys.stdin.readline

n,k=map(int,input().split())

result=[]
circle=[True for n in range(n)]
target=-1

for i in range(n):
    count=0
    while(count<k):
        target=(target+1)%n
        if circle[target]:
            count+=1
    circle[target]=False
    result.append(target+1)
        
print("<" + ", ".join(map(str,result)) + ">")

'''
