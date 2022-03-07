"""
Date    : 2022.03.06
Update  : 2022.03.07
Source  : 22857.py
Purpose : 투 포인터
url     : https://www.acmicpc.net/problem/22857
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    s = list(map(int, input().split()))

    p2 = 0
    answer = 0
    odd = 0
    even = 0

    for p1 in range(n):
        while odd <= k and p2 < n:
            if s[p2] % 2 == 0:
                even += 1
            else:
                odd += 1
            p2 += 1

        if odd <= k+1 and even > answer:
            answer = even

        if s[p1] % 2 == 0:
            even -= 1
        else:
            odd -= 1

    print(answer)