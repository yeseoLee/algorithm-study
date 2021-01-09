import sys
line=sys.stdin.readline()
cnt=0
i=0
while(i<len(line)-1):
    if(line[i:i+2]=="c="or line[i:i+2]=="c-"
       or line[i:i+2]=="d-"or line[i:i+2]=="lj"
       or line[i:i+2]=="nj"or line[i:i+2]=="s="
       or line[i:i+2]=="z="):
        i+=2
    elif(line[i:i+3]=="dz="):
        i+=3
    else:
        i+=1
    cnt+=1

print(cnt)

"""모범답안
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
b = input()
for i in a:
    b = b.replace(i, '0')
print(len(b))
replace는 문자열에서 어떠한 값을 찾아 변경해 주는 역할을 한다.
"""
