#레벨슈타인 거리 구하기
def calc_distance(a: str , b: str):
    if a==b: return 0
    a_len=len(a)
    b_len=len(b)
    if a=="" : return b_len
    if b=="" : return a_len

    #2차원 매트릭스 (a_len+1, b_len+1)
    matrix=[[0 for j in range(b_len+1)] for i in range(a_len+1)]

    #첫 번째 행, 첫 번째 열을  문자열 길이로 초기화
    for i in range(a_len+1):
        matrix[i][0]=i
    for j in range(b_len+1):
        matrix[0][j]=j

    for i in range(1, a_len+1):
        ac=a[i-1] #비교할 문자
        for j in range(1, b_len+1):
            bc=b[j-1] #비교할 문자
            cost = 0 if (ac==bc) else 1 #같으면 비용 0, 다르면 비용 1
            matrix[i][j]=min([
                matrix[i-1][j]+1, #문자 삽입
                matrix[i][j-1]+1, #문자 제거
                matrix[i-1][j-1]+cost #문자 변경
            ])

    return matrix[a_len][b_len]


#example
samples = ["신촌역","신천군","신천역","신발","마곡역"]
base = samples[0]
r = sorted(samples, key = lambda x : calc_distance(base,x))
for x in r:
    print(calc_distance(base,x),x)
