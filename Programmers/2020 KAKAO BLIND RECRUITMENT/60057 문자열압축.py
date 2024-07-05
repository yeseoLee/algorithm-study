def solution(s):
    min_answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        count = 1
        now = ""
        debug = ""
        for j in range(0, len(s) + 1, i):
            if j + i > len(s):
                if count != 1:
                    debug += str(count)
                debug += now
                debug += s[j:]
                break
            if now == s[j : j + i]:
                count += 1
            else:
                if count == 1:
                    debug += now
                else:
                    debug += str(count) + now
                now = s[j : j + i]
                count = 1
        min_answer = min(min_answer, len(debug))
    return min_answer
