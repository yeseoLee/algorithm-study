""" 이항 계수 문제
#nCk = n!/((n-k)!*k!)
1. 곱하는 횟수를 줄이기 nCk vs nC(n-k)

n,k=map(int,input().split())
result=1
k= k if k<n-k else n-k
for i in range(k):
    result*=n//(i+1)
    n+=-1
print(result)

2. 파스칼의 삼각형 분할정복 nCk = (n-1)C(k-1) + (n-1)Ck
def nCk(n,k):
    if(k==0 or n==1 or n==k):
        return 1
    else:
        return nCk(n-1,k-1)+nCk(n-1,k)

n,k=map(int,input().split())
k= k if k<n-k else n-k
result=nCk(n,k)
print(result%1000000007)

3.
"""
