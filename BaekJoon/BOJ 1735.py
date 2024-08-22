import math

a, b = map(int, input().split())
c, d = map(int, input().split())

numerator, denominato = a * d + b * c, b * d
n, m = 2, int(math.sqrt(min(numerator, denominato)) + 1)

while n <= m:
    if numerator % n == 0 and denominato % n == 0:
        numerator //= n
        denominato //= n
    else:
        n += 1

print(numerator, denominato)
