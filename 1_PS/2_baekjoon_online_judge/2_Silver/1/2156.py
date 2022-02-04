"""
Date    : 2022.02.04
Update  : 2022.02.04
Source  : 2156.py
Purpose : dp
url     : https://www.acmicpc.net/problem/2156
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import sys

input = sys.stdin.readline
MAX_GLASS = 10001

if __name__ == "__main__":
    n = int(input())
    grapes = [0 for _ in range(MAX_GLASS)]
    dp = [0 for _ in range(MAX_GLASS)]

    for i in range(n):
        temp = int(input())
        grapes[i] = temp

    dp[0] = grapes[0]
    dp[1] = grapes[0] + grapes[1]
    dp[2] = max(dp[0], grapes[1]) + grapes[2]

    for i in range(3, n):
        dp[i] = max(dp[i-1], grapes[i] + grapes[i-1] + dp[i-3])

    print(dp[n-1])

"""
반례

6
100
100
1
1
100
100

정답 : 400
output : 301
"""