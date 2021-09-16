# # Ch8_DP_바닥 공사
#
# n = int(input())
#
# dp = [0] * (n)
# dp[0] = 1
# dp[1] = 3
#
# for i in range(2, n):
#     dp[i] = dp[i-1] + dp[i-2]*2
#
# print(dp[n-1]%796796)
#
# # 14분 21초

# # Ch8_DP_효율적인 화폐 구성
#
# n, m = list(map(int, input().split()))
# coins = []
# dp = [1e9] * (m+1)
# dp[0] = 0
#
# for i in range(n):
#     coins.append(int(input()))
#
# for coin in coins:
#     for i in range(coin, m+1):
#         dp[i] = min(dp[i-coin]+1, dp[i])
#
# if dp[m] >= 1e9:
#     print(-1)
# else:
#     print(dp[m])
#
# # 14분 11초