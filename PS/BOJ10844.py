import sys
n= int(sys.stdin.readline())
dp=[1 for i in range(10)]
dp[0]=0

for i in range(1,n):
    tmp=[0 for i in range(10)]
    for i in range(1,9):
        tmp[i]=dp[i-1]+dp[i+1]
    tmp[0]=dp[1]
    tmp[9]=dp[8]
    dp=tmp

a=1000000000
print(sum(dp)%a)

"""
1.처음엔 각 자리수별 개수로 풀려다 실패
2. dp[k]에 k자리수별 모든 원소를 저장해서 메모리 초과
3. dp[k]에 k자리수 별 모든 원소의 마지막수를 저장해서 메모리 초과
4. tmp[]를 이용해서 1차원 배열 dp에 계속 덮어씌웠으나 메모리 초과
5. dp[10] 인덱스를 원소 끝자리수로 이용하여 각각의 개수를 저장
ex) dp[0]->0으로 끝나는 수의 개수
"""
