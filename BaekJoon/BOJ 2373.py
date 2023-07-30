# BOJ 2373 Fibonacci Game
N=int(input())

def play(n):
    num = -1 
    return num

print(play(N))

''' 
승리조건
- max >= given
- given: 2
- given: 4
- given: 6
- givne: 7
- given: 9
...
DP로 풀기
가져가는 수 K와 남은 수 M 으로 연산하여
K가 가능한 수인지 체크
ex) 2*K >= M 이거나 M이 무조건 이기는 수
'''
