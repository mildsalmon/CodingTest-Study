"""
Date    : 2022.02.06
Update  : 2022.02.06
Source  : 2579.py
Purpose : DP
url     : https://www.acmicpc.net/problem/2579
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

if __name__ == "__main__":
    n = int(input())
    stairs = [0 for _ in range(301)]
    dp = [0 for _ in range(301)]

    for i in range(n):
        stairs[i] = int(input())

    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0], stairs[1]) + stairs[2]

    for i in range(3, n):
        dp[i] = max(stairs[i-1] + dp[i-3], dp[i-2]) + stairs[i]

    print(dp[n-1])