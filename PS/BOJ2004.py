"""메모리 부족 나온 처음 코드"""
import sys
def getK(n,k):
    cnt=0
    tmp=n
    while(tmp):
        tmp//=k
        cnt+=tmp
    return pow(k,cnt)

n,m=map(int,sys.stdin.readline().split())
nf=(getK(n,2)*getK(n,5))
mf=(getK(m,2)*getK(m,5))
nmf=(getK(n-m,2)*getK(n-m,5))

ncm=str(nf//(mf*nmf))
print(len(ncm)-1)


"""모범답안"""
import sys
def getK(n,k):
    cnt=0
    tmp=n
    while(tmp):
        tmp//=k
        cnt+=tmp
    return cnt

n,m=map(int,sys.stdin.readline().split())
ncm2=getK(n,2)-getK(m,2)-getK(n-m,2)
ncm5=getK(n,5)-getK(m,5)-getK(n-m,5)

print(min(ncm2,ncm5))
