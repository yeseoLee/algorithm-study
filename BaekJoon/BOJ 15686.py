from collections import defaultdict
n,m=map(int,input().split()) #N*N, 치킨집 M개

#0:빈칸, 1:집 , 2:치킨집
arr=[list(map(int,input().split())) for _ in range(n)]
cost=defaultdict(int)

#치킨거리의 합을 최소로 하는 치킨집 M개

chicken=[]
house=[]
for i in range(n):
    for j in range(n):
        if(arr[i][j]==1):
            house.append((i,j))
        if(arr[i][j]==2):
            chicken.append((i,j))

if(len(chicken)==m):
    print()
else:
    for i,j in house:
        minI,minJ=-1,-1
        minD=float('inf')
        for ci, cj in chicken:
            dis=abs(i-ci)+abs(j-cj)
            if(dis < minD):
                print(ci,cj)
                minI,minJ=ci,cj
                minD=dis
        cost[(minI,minJ)]+=minD
    for key,val in sorted(cost.items())[:m]:
        print(key,val)
    


            
