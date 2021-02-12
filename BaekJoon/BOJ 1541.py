import sys
line= sys.stdin.readline()
a=[]
s=0
for i in range(len(line)):
    if(line[i]=='+' or line[i]=='-'):
        a.append(int(line[s:i]))
        a.append(line[i])
        s=i+1
    elif(line[i]=='\n'):
        a.append(int(line[s:i]))

result=0
tmp=0
f=0
for i in a:
    if(i=='-'):
        if(f==0): f=1
        else:
            result-=tmp
            tmp=0
    elif(i!='+' and i!='-'):
        if(f==0):
            result+=i
        else:
            tmp+=i
            
result-=tmp
print(result)

"""
'-'가 나오기 전 모든 수를 더하고
나온 이후  모든 수를 빼주면 된다.
따라서 다시 풀어보았다.
"""
import sys
line= sys.stdin.readline()
a=[]
s=0
result=0
for i in range(len(line)):
    if(line[i]=='+' or line[i]=='-'):
        a.append(int(line[s:i]))
        a.append(line[i])
        s=i+1
    elif(line[i]=='\n'):
        a.append(int(line[s:i]))
        
for i in range(len(a)):
    if(a[i]=='-'):
        for j in range(i+1,len(a)):
            if(a[j]!='-' and a[j]!='+'):
                result-=a[j]
        break
    elif(a[i]!='-' and a[i]!='+'):
        result+=a[i]
print(result)

"""
실행속도가 더 느리게 나와서
모범답안을 찾아보았고, 아래 코드이다.
"""
line=sys.stdin.readline().split('-')
s=0

for i in line[0].split('+'):
    s+=int(i)
for i in line[1:]:
    for j in i.split('+'):
        s-=int(j)
print(s)
