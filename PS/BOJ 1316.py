import sys
n=int(sys.stdin.readline())
cnt=0
for i in range(n):
    line=sys.stdin.readline()
    a=[]
    f=1
    for j in range(len(line)):
        if(line[j] in a):
            if(line[j-1]!=line[j]):
                f=0
        else:
            a.append(line[j])
    if(f==1):
        cnt+=1
print(cnt)

"""모범답안 1.
n=int(input())
cnt=0
for i in range(n):
    word=input()
    for j in range(len(word)):
        if j!=len(word)-1: #마지막 문자가 아니면
            if(word[j]==word[j+1]): #문자가 연속해서 나올 때
                pass
            else:
                if(word[j] in word[j+1:]: #앞서 나온 문자가 뒤에 존재할 때
                   break
        else: #중간에 break 되지 않고 마지막 문자에 도달
            cnt+=1
print(cnt)

모범답안 2. for-else
import sys
n=int(sys.stdin.readline())
cnt=0
for i in range(n):
    line=sys.stdin.readline()
    a=[]
    f=1
    for j in range(len(line)):
        if(line[j] in a):
            if(line[j-1]!=line[j]):
                break
        else:
            a.append(line[j])
    else:
        cnt+=1
print(cnt)
"""


