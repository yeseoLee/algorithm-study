import sys
input = sys.stdin.readline

N = int(input())
MOD = 1000000

period = (MOD // 10) * 15
fibonacci = [0, 1]

for i in range(1, period):
    num = (fibonacci[i-1] + fibonacci[i]) % MOD
    fibonacci.append(num)

print(fibonacci[N % period])
