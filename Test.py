def power(a,b,c):
    if b == 1:
        return a % c
    else:
        temp = power(a, b // 2) # a^(b // 2)를 미리 구한다.
        # b가 짝수 (a^(b//2)) * (a^(b//2)) = a^b
        if b % 2 == 0:
            return temp * temp % c 
        # b가 홀수 (a^(b//2)) * (a^(b//2)) * a = a^b
        else:    
            return temp * temp * a % c 

A,B,C= map(int, input().split())
result = power(A,B,C)
print(result)

