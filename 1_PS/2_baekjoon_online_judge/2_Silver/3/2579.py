"""
Date    : 2022.02.03
Update  : 2022.02.03
Source  : 2579.py
Purpose :
url     : https://www.acmicpc.net/problem/2579
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import sys

input = sys.stdin.readline

def dp(stairs):
    global n

    dp = [0 for _ in range(n)]

    if n <= 2:
        return sum(stairs[:])

    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0], stairs[1]) + stairs[2]

    for i in range(3, n):
        dp[i] = max(stairs[i-1] + dp[i-3], dp[i-2]) + stairs[i]

    return dp[n-1]


if __name__ == "__main__":
    n = int(input())
    stairs = []

    for _ in range(n):
        temp = int(input())
        stairs.append(temp)

    print(dp(stairs))