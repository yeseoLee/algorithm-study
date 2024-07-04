def solution(s):
    answer = []

    flag = True
    for ch in s.lower():
        if ch == " ":
            flag = True
        elif flag:
            flag = False
            if ord("a") <= ord(ch) and ord(ch) <= ord("z"):
                ch = chr(ord(ch) + ord("A") - ord("a"))
        answer.append(ch)

    return "".join(answer)
