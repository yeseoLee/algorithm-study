import sys

t=int(sys.stdin.readline())
for i in range(t):
    avg=0
    above_avg=0
    line=list(map(int,sys.stdin.readline().split()))
    for i in range(1,line[0]+1):
        avg+=line[i]
    avg/=line[0]
    for i in range(1,line[0]+1):
        if(line[i]>avg):
            above_avg+=1
    above_avg=(above_avg/line[0])*100
    print("%.3lf%%"%(above_avg))
