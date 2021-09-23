def balance(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        elif p[i] == ")":
            count -= 1

        if count == 0:
            return i + 1


def right_str(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            if count == 0:
                return False
            return True


def solution(p):
    if len(p) == 0:
        return p

    b_index = balance(p)

    u = p[:b_index]
    v = p[b_index:]

    if right_str(u) == True:
        temp = u + solution(v)
    else:
        temp = "("
        temp += solution(v)
        temp += ")"

        u = u[1:-1]

        for i in u:
            if i == "(":
                temp += ")"
            else:
                temp += "("

    return temp

print(solution("(()())()"))