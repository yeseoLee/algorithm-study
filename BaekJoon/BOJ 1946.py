import sys

t=int(sys.stdin.readline()) #Test Case
for _ in range(t):
    n=int(sys.stdin.readline()) #지원자 수
    arr=[] # 지원자들의 순위
    count=1 #합격자 수
    for i in range(n):
        s,m=map(int,sys.stdin.readline().split()) #서류순위, 면접순위
        arr.append([s,m])
    arr=sorted(arr, key= lambda x: x[0])
    print(arr)
    min_m=arr[0][1]
    for i in range(1,n):
        #if(min_m<arr[i][1]): #서류,면접 둘다 못봄-> 탈락
        if(min_m>arr[i][1]): #서류 잘본 애들보다 면접 잘봄 ->합격
            min_m=arr[i][1]
            count+=1
    print(count)
            
        
