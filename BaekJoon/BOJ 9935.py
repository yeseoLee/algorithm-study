import sys
input = sys.stdin.readline

normal_str=input().rstrip()
explosive_str=list(input().rstrip())

ex_len=len(explosive_str)
que=[]

for i in normal_str:
    que.append(i)
    if(i==explosive_str[-1]):
        if que[-ex_len:]==explosive_str:
            #que=que[:len(que)-ex_len]
            del que[-ex_len:]

if(que):
    print(''.join(que))
    #print(*que, sep="")
else:
    print("FRULA")

'''
import sys
input=sys.stdin.readline
normal_str=input().rstrip()
explosive_str=list(input().rstrip())

ex_len=len(explosive_str)
que=[]

for i in normal_str:
    que.append(i)
    if (que[-ex_len:]==explosive_str):
        del que[-ex_len:]

if(que==[]):
    print("FRULA")
else:
    print(''.join(que))
'''
