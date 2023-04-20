import sys
input = sys.stdin.readline 

RED = [3,3,3,6,6,6]
GREEN = [1,1,1,4,4,4]
WHITE = [2,2,5,5,5,5]

# case 1: GREEN VS WHITE

cnt_all = 0
cnt_green_win = 0
cnt_white_win = 0
cnt_draw = 0

for r in GREEN:
    for w in WHITE:
        cnt_all += 1
        if r>w: cnt_green_win += 1
        elif r<w: cnt_white_win+=1
        else: cnt_draw+=1

print(f"전체: {cnt_all}, 그린 승리: {cnt_green_win}, 화이트 승리: {cnt_white_win}, 무승부: {cnt_draw}")

print(f"GREEN이 White를 이길 확률: {cnt_green_win/cnt_all}")
# case 2: RED VS GREEN