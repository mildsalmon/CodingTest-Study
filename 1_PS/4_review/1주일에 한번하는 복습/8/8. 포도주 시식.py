"""
Date    : 2022.02.06
Update  : 2022.02.06
Source  : 2156.py
Purpose : DP
url     : https://www.acmicpc.net/problem/2156
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import sys

input = sys.stdin.readline
MAX_WINE = 10001

if __name__ == "__main__":
    n = int(input())
    wines = [0 for _ in range(MAX_WINE)]
    dp = [0 for _ in range(MAX_WINE)]

    for i in range(n):
        wines[i] = int(input())

    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]
    dp[2] = max(dp[1], wines[0] + wines[2], wines[1] + wines[2])

    for i in range(3, n):
        dp[i] = max(dp[i-1], wines[i] + wines[i-1] + dp[i-3], wines[i] + dp[i-2])

    print(dp[n-1])