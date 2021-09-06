# # Ch8_DP_바닥 공사
#
# n = int(input())
#
# dp = [0] * (n+1)
# dp[1] = 1
# dp[2] = 3
#
# for i in range(3, n+1):
#     dp[i] = max(dp[i], dp[i-1] + 2*dp[i-2])
#
# print(dp[i]%796796)
#
# # 10분 23초

# ch8_DP_효율적인 화폐 구성

n, m = list(map(int, input().split()))
coin = []
INF = 1e9
dp = [INF] * (m+1)
dp[0] = 0

for i in range(n):
    coin.append(int(input()))

for i in coin:
    for j in range(m+1):
        dp[j] = min(dp[j], dp[j-i]+1)
        # print(dp)
print(dp[m])

# 15분 / Pass