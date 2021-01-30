def power(a,b):
    if b == 1:
        return a % C
    else:
        temp = power(a, b // 2) # a^(b // 2)를 미리 구한다.
        if b % 2 == 0:
            return temp * temp % C # b가 짝수 (a^(b//2)) * (a^(b//2)) = a^b
        else: 
            return temp * temp * a % C # b가 홀수 (a^(b//2)) * (a^(b//2)) * a = a^b

A, B, C = map(int, input().split())
result = power(A, B)
print(result)

""" 내코드 
import sys
a,b,c=map(int,sys.stdin.readline().split())
r=a%c
result=pow(r,b)%c
print(result)
숫자가 커지는게 문제가 아니라 연산 횟수가 많아지는게 문제였다.
따라서 곱셈의 반복횟수를 줄여주는게 핵심이였는데 접근이 이상했었다.
"""
