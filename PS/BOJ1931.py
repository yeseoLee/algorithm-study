import sys
n=int(sys.stdin.readline())
timeline = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
timeline = sorted(timeline,key = lambda x: ((x[1],x[0])))
cnt=0
last=0
for i,j in timeline:
    if(i>=last):
        cnt+=1
        last=j
print(cnt)
