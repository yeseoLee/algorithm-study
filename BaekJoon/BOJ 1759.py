#최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
#알파벳이 암호에서 증가하는 순서로 배열
#서로 다른 L개의 알파벳 소문자들로 구성
#암호로 사용했을 법한 문자의 종류는 C가지

import sys
from itertools import combinations
input=sys.stdin.readline

l,c=map(int,input().split())
possible=sorted(input().split())

def vowel_count(code):
    vowel=['a','e','i','o','u']
    count=0
    for i in code:
        if i in vowel:
            count+=1
    return count
codes = combinations(possible,l)
for code in codes:
    if 1<= vowel_count(code) <= l-2:
        print(''.join(code))
