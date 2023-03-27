import sys
input = sys.stdin.readline

def change(x: int) -> int :
    return (x+1)%2

switch_cnt = int(input())
state= list(map(int,input().split()))

student_cnt = int(input())
for i in range(student_cnt):
    gender,number = map(int,input().split())
    if gender == 1: # 남학생 
        for i in range(number-1,switch_cnt,number):
            state[i] = change(state[i])
    elif gender == 2: # 여학생
        state[number-1] = change(state[number-1])
        limit = min(number, switch_cnt-number+1)
        for i in range(1,limit):
            if state[number-1-i]!=state[number-1+i]:
                break
            state[number-1-i] = change(state[number-1-i])
            state[number-1+i] = change(state[number-1+i])               
    else: # 예외
        continue       

if(switch_cnt>0):
    print(*state[:20])
if(switch_cnt>20):
    print(*state[20:40])
if(switch_cnt>40):
    print(*state[40:60])
if(switch_cnt>60):
    print(*state[60:80])
if(switch_cnt>80):
    print(*state[80:100])