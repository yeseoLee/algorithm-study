arr = [1,2,3]
n = len(arr)

for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            pass
            print(arr[j], end=' ')
    print()

'''
1 
2 
1 2 
3 
1 3 
2 3 
1 2 3
'''
