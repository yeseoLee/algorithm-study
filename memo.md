### 한줄 PS일기

날짜 | 내용
------------ | ------------- 
11/01 | ```print("hello world") ```
11/02 | input 보다 sys.stdin.readline()이 빠르다. input쓰면 종종 시간초과난다.
11/03 | 만약 여러 줄을 입력받고 싶으면 sys.stdin을 이용하자. ^Z를 입력받으면 종료해주기 때문에 임의의 여러 줄을 입력받아야 하는 문제에서 유용하다.
11/04 | 소수점 반올림은 음수/양수일 때 따져야한다. 그냥 round() 써도되고.
11/05 | 오름차순 또는 내림차순 등의 정렬에서 정렬 조건이 여러 개일 경우(비교할 아이템의 요소가 복수 개일 경우), 튜플로 그 순서를 내보내주면 된다.  
 || ex. sorted(e, key = lambda x : (x[0], -x[1])) (-를 붙이면, 현재 정렬차순과 반대로 하게 된다.)
 11/14 | n 개의 정수를 입력받아 리스트에 저장할 때 a=[int(sys.stdin.readline())) for i in range(n)]
11/15 | from collections import Counter -> 문자열에서 문자 개수 셀 때, 배열에서 같은 값 개수 셀 때 유용하다. 사용법을 잘 익혀두자.
11/16 | list = str.split() : 문자열 -> 리스트 ''.join( list ) : 리스트 -> 문자열
|| print('\n'.join([''.join([str(i) for i in row]) for row in arr]))
11/17 | .format함수 (문자열 포매팅, 자바스크립트 닮았다)
