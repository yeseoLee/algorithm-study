import sys
n=int(sys.stdin.readline())
p=list(map(int,sys.stdin.readline().split()))
p.sort()
time=0
now=0
for i in p:
    now+=i
    time+=now
    
print(time)
