a=int(input(),2)
b=int(input(),2)

n = 100000
mask = 2 ** n - 1
# A & B, A | B, A ^ B, ~A, ~B

print(f'{a&b:0{n}b}')
print(f'{a|b:0{n}b}')
print(f'{a^b:0{n}b}')
print(f'{mask-a:0{n}b}')
print(f'{mask-b:0{n}b}')
