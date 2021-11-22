from collections import Counter
n=list(input())

for i in range(len(n)):
    if n[i]=='9': n[i]='6'
counter=Counter(n)
if counter['6']:
    counter['6']=(counter['6']+1) // 2
print(counter.most_common(1)[0][1])
