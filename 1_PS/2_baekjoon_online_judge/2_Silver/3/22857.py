"""
Date    : 2022.03.06
Update  : 2022.03.06
Source  : 22857.py
Purpose :
url     : https://www.acmicpc.net/problem/22857
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    s = list(map(int, input().split()))

    p1, p2 = 0, 0
    answer = 0

    if s[p2] % 2 == 1:
        odd = 1
        p2 += 1
    else:
        odd = 0


    for p1 in range(n):
        while p2 < n:
            if s[p2] % 2 == 1:
                odd += 1
            if odd <= k:
                p2 += 1
            else:
                odd -= 1
                break

        p2 -= 1

        answer = max(answer, p2-p1+1-odd)

        if s[p1] % 2 == 1:
            odd -= 1

    print(answer)