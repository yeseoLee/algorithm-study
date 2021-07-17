import sys
import re
import itertools
input=sys.stdin.readline
n,k=map(int,input().split())
arr=[input().strip()[4:-4] for _ in range(n)]

if(k<5):
    print(0)
    sys.exit()

arr=[re.sub('[acint]','',word) for word in arr] #기본 문자 제거
'''
#중복 문자 제거 & 읽을 수 없는 문자 제거
arr=[''.join((set(word))) for word in arr if len(set(word))<=k-5] 
'''

apb=[] #available alphabet
for i in arr:
    apb=apb+list(i)
apb = list(set(apb))

# words : 각 단어의 비트마스킹한 정수를 저장
words=[]
for i in arr:
    x=0
    for j in i:
        x |= (1 << (ord(j)- ord('a')))
    words.append(x)

#전부 다 읽을 수 있음
if(len(apb)<=k-5):
    print(len(arr))
else:
    ans=0
    for i in list(itertools.combinations(apb, k - 5)):
        mask=0
        cnt = 0
        for j in i:
            mask |= (1 << (ord(j) - ord('a')))
            
        # 단어와 각 조합의 비교
        for word in words:
            if mask & word == word:
                cnt += 1
        ans=max(ans,cnt)
    print(ans)


'''
import sys
import re
import itertools
input=sys.stdin.readline
n,k=map(int,input().split())
arr=[input().strip()[4:-4] for _ in range(n)]

if(k<5):
    print(0)
    sys.exit()

arr=[re.sub('[acint]','',word) for word in arr] #기본 문자 제거
arr=[''.join((set(word))) for word in arr
         if len(set(word))<=k-5] #중복 문자 제거 & 읽을 수 없는 문자 제거
    
apb=[] #abailable alphabet
for i in arr:
    apb=apb+list(i)
apb = list(set(apb))

#전부 다 읽을 수 있음
if(len(apb)<=k-5):
    print(len(arr))
else:
    max_cnt=0
    for mask in list(itertools.combinations(apb,k-5)):
        cnt=0
        for word in arr:
            if word in mask:
                cnt+=1
        max_cnt=max(max_cnt,cnt)
    print(max_cnt)
'''
