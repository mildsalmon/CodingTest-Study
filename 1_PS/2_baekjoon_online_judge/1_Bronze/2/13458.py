"""
Date    : 2022.03.01
Update  : 2022.03.05
Source  : 13458.py
Purpose : 수학
url     : https://www.acmicpc.net/problem/13458
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    B, C = list(map(int, input().split()))
    cnt = 0

    for i in range(n):
        A[i] -= B
        cnt += 1

        if A[i] > 0:
            if A[i] % C == 0:
                cnt += A[i] // C
            else:
                cnt += A[i] // C + 1

    print(cnt)