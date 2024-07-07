def solution(genres, plays):
    answer = []

    dic_genres = {}
    dic_plays = {}

    for i in range(len(genres)):
        if genres[i] not in dic_genres:
            dic_genres[genres[i]] = 0
        if genres[i] not in dic_plays:
            dic_plays[genres[i]] = []

        dic_genres[genres[i]] += plays[i]
        dic_plays[genres[i]].append((i, plays[i]))

    for key, val in sorted(dic_genres.items(), key=lambda item: -item[1]):
        for val in sorted(dic_plays[key], key=lambda x: (-x[1], x[0]))[:2]:
            answer.append(val[0])

    # 장르 -> 재생 -> 고유번호 순으로 정렬
    return answer
