import sys
t=int(sys.stdin.readline()) #Test Case
for _ in range(t):
    length,n=map(int,sys.stdin.readline().split()) #막대길이, 개미의 수
    pos=[int(sys.stdin.readline()) for x in range(n)] #개미위치
    pos=sorted(pos)

    #최소시간
    if(pos[0]>=length//2):
        min_time=length-pos[0]
    elif(pos[-1]<=length//2):
        min_time=pos[-1]
    else:
        for i in range(n):
            if(pos[i]>=length//2):
                min_time=max(pos[i-1],length-pos[i])
                break
    #최대시간
    max_time=max(length-pos[0],pos[-1])
    print(min_time,max_time)      
