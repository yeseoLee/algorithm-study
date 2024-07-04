def solution(p):
    def is_correct(w):
        stack = []
        for ch in w:
            if ch == ")":
                if not stack:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0

    def split_uv(w):
        o, c = 0, 0
        for i in range(len(w)):
            if w[i] == "(":
                o += 1
            else:
                c += 1
            if o == c:
                return w[: i + 1], w[i + 1 :]
        return w, ""

    def reverse_bracket(w):
        new_w = []
        for ch in w:
            if ch == "(":
                new_w.append(")")
            else:
                new_w.append("(")
        return "".join(new_w)

    # 1
    if not p:
        return p
    # 2
    u, v = split_uv(p)
    # 3
    if is_correct(u):
        return u + solution(v)
    # 4
    else:
        # 4-1
        result = "("
        # 4-2
        result += solution(v)
        # 4-3
        result += ")"
        # 4-4
        result += reverse_bracket(u[1:-1])
        return result
