"""
Date    : 2021.12.21
Update  : 2021.12.21
Source  : 12919.py
Purpose : 완전탐색으로 풀어서 시간초과가 발생했다.
url     : https://www.acmicpc.net/problem/12919
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def dfs(t, s):
    global answer

    s_len = len(s)


    if len(t) == s_len:
        if ''.join(t) == s:
            answer = True
        return

    if t[0] == "B":
        temp = t[::-1]
        temp.pop()
        dfs(temp, s)

    if t[-1] == "A":
        temp = t[:]
        temp.pop()
        dfs(temp, s)


if __name__ == "__main__":
    S = input()
    T = list(input())

    answer = False

    dfs(T, S)

    if answer:
        print(1)
    else:
        print(0)
