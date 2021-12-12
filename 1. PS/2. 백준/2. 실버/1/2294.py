"""
Date    : 2021.12.11
Update  : 2021.12.11
Source  : 2294.py
Purpose : 단순 DP를 이용한 풀이.
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

n, k = list(map(int, input().split()))
coins = []
dp = [1e9] * (k+1)

for i in range(n):
    coins.append(int(input()))

dp[0] = 0

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)
    # print(dp)

if dp[-1] != 1e9:
    print(dp[-1])
else:
    print(-1)