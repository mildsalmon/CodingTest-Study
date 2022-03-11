"""
Date    : 2022.03.06
Update  : 2022.03.11
Source  : 22857.py
Purpose : 투 포인터
url     : https://www.acmicpc.net/problem/22857
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    S = list(map(int, input().split()))

    right = 0
    even = 0
    odd = 0
    len_continuously_array = 0

    for left in range(n):
        while right < n and odd <= k:
            if S[right] % 2 == 0:
                # 짝수
                even += 1
            else:
                # 홀수
                odd += 1
            right += 1

        len_continuously_array = max(len_continuously_array, even)

        if S[left] % 2 == 0:
            even -= 1
        else:
            odd -= 1

    print(len_continuously_array)
