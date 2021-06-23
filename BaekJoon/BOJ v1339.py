#각 알파벳별로 계수를 구한다음 계수가 큰 순서대로 정렬
n=int(input())
apb=[0]*26
words=[]
for i in range(n):
    words.append(list(input()))

for word in words:
    lw=len(word)
    for i in range(lw):
        apb[ord(word[i])-ord('A')]+=10**(lw-i-1)

apb=sorted(apb,reverse=True) # 어떤 알파벳인지는 중요하지 않음
max_sum=0
for i in range(10):
    max_sum+=apb[i]*(9-i)

print(max_sum)


        

