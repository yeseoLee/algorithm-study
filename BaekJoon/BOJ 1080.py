n,m=map(int,input().split())
a=[list(input()) for _ in range(n)]
b=[list(input()) for _ in range(n)]

cnt=0
for i in range(n-2):
    for j in range(m-2):
        #의도한 점(선택)에 대해서 다르면 바꿔줌
        if(a[i][j]!=b[i][j]):
            cnt+=1
            #의도하지 않은(선택할 수 없는) 나머지 점들도 규칙에 따라 바뀜
            for col in range(i,i+3):
                for row in range(j,j+3):
                    if(a[col][row]=='0'): a[col][row]='1'
                    else: a[col][row]='0'

#의도한 점들을 모두 올바르게 바꿨을 때, 의도하지 않은 점들도 옳게 바뀌었는지 검사
for i in range(n):
    for j in range(m):
        if(a[i][j]!=b[i][j]):
            cnt=-1
            break
print(cnt)











