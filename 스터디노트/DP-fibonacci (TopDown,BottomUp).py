#dynamic programming - fibonacci

#1.recursive
def fibonacci(n):
    if(n<=2):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#2.dp: Top-Down
fibo=[0]*n # 메모이제이션
def fibonacci(n):
    if(n<=2):
        return 1
    if(fibo[n]==0): #아직 계산되지 않은 값
        fibo[n]=fibonacci(n-1)+fibonacci(n-2)
    return fibo[n] #이미 알고있는 값은 바로 사용
#3.dp: Bottom-Up
fibo=[0]*n
def fibonacci(n):
    fibo[1]=1
    for i in range(2,n+1):
        fibo[i]=fibo[i-1]+fibo[i-2]
    return fibo[n]
