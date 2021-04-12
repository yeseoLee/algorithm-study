n,h=map(int,input().split())
arr=[int(input()) for i in range(n)] #장애물 크기

#장애물 홀수/짝수 분리, 테이블 생성
even=[0]*(h)
odd=[0]*(h)
for i in range(n):
    if(i%2==0):
        even[arr[i]-1]+=1
    else:
        odd[arr[i]-1]+=1
        
#누적 테이블 생성-길이가 짧은 장애물로 값이 누적되도록
e,o=0,0
for i in range(h-1,-1,-1):
    odd[i]+=o
    o=odd[i]
    even[i]+=e
    e=even[i]

#짝수 테이블은 뒤집어준다(거꾸로 매달려있는 장애물)
even=list(reversed(even))

# 파괴 장애물 카운트 및 최솟값 출력
min_cnt=n
min_cnt_cnt=0
for i in range(h):
    if(even[i]+odd[i] < min_cnt):
        min_cnt=even[i]+odd[i]
        min_cnt_cnt=1
    elif(even[i]+odd[i] == min_cnt):
        min_cnt_cnt+=1
    
print(min_cnt,min_cnt_cnt)

''' Time Limit
n,h=map(int,input().split())
arr=[int(input()) for i in range(n)] #장애물 크기

#장애물 홀수/짝수 분리, 중복제거 & 정렬
odd=sorted(arr[0::2],reverse=True)
odd.append(0)
even=sorted(arr[1::2],reverse=True)

min_cnt=n
min_cnt_cnt=0
before_i=0
for idx,i in enumerate (odd):
    if(before_i>=i):
        pass
    cnt=n//2+idx
    for j in even:
        if(j<(h-i)):
            cnt-=1
    if(cnt<min_cnt):
        min_cnt=cnt
        min_cnt_cnt=1
    elif(cnt==min_cnt):
        min_cnt_cnt+=1
    before_i=i

print(min_cnt,min_cnt_cnt)
'''
