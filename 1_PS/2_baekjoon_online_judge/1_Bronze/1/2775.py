"""
Date    : 2022.04.08
Update  : 2022.04.08
Source  : 2775.py
Purpose : dp / list comprehension
url     : https://www.acmicpc.net/problem/2775
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import sys

input = sys.stdin.readline

# 0층 ~ 14층 / 1호 ~ 14호
dp = [[j+1 for j in range(14)] if i == 0 else [1 if k == 0 else 0 for k in range(14)] for i in range(15)]

for i in range(1, 15):
    for j in range(1, 14):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

for _ in range(int(input())):
    k = int(input())
    n = int(input())

    print(dp[k][n-1])