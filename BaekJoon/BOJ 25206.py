import sys

input = sys.stdin.readline


grade_dic={"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0,}
def grade_to_num(grade:str)-> float:
    if grade not in grade_dic:
        print("ERROR")
        return -1.0
    return grade_dic[grade]
    

T = 20
credit = 0
grade = 0
for _ in range(T):
    a,b,c = input().split()
    if c=='P':
        continue
    
    credit += float(b)
    grade += float(b) * grade_to_num(c)

print(grade/credit)

    

