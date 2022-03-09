"""
Date    : 2022.03.09
Update  : 2022.03.09
Source  : 21940.py
Purpose : 플로이드-와샬
url     : https://www.acmicpc.net/problem/21940
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    s = [list(map(lambda x: int(x)-1, input().split()))]
    d = list(map(lambda x: int(x)-1, input().split()))

    temp = [0 for _ in range(n)]
    save_s = s[-1][:]
    loop = m+1

    for tc in range(m):
        for i, x in enumerate(d):
            temp[x] = s[-1][i]

        s.append(temp[:])

        if save_s[:] == s[-1][:]:
            loop = tc+1
            break

    print(s)
    print(*map(lambda x: int(x)+1, s[m%loop]))
