"""
Date    : 2021.12.21
Update  : 2021.12.21
Source  : 12919.py
Purpose : 완전탐색으로 풀어서 시간초과가 발생했다.
url     : https://www.acmicpc.net/problem/12919
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def dfs(s, t, answer):
    global t_len

    if not answer:
        if len(s) == t_len:
            if s == t:
                answer = True
            return answer

        if not answer:
            temp = s+"A"
            answer = dfs(temp, t, answer)
            temp = s+"B"
            answer = dfs(temp[::-1], t, answer)

    return answer

if __name__ == "__main__":
    S = input()
    T = input()

    t_len = len(T)

    answer = dfs(S, T, False)

    if answer:
        print(1)
    else:
        print(0)

