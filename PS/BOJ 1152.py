import sys
line=sys.stdin.readline()
cnt=1

for i in range(1,len(line)-2):
    if(line[i]==' '):
        cnt+=1
if(line==" \n"):
    print("0")
else:
    print(cnt)

"""
import sys
line=sys.stdin.readline().split()
print(len(line))
"""

