# # Ch8_DP_1로 만들기
#
# x = int(input())
# dp = [1e9] * (x+1)
#
# dp[0] = 0
# dp[1] = 0
#
# for i in range(2, x+1):
#     dp[i] = min(dp[i-1]+1, dp[i])
#
#     if i % 2 == 0:
#         dp[i] = min(dp[i//2]+1, dp[i])
#     if i % 3 == 0:
#         dp[i] = min(dp[i//3]+1, dp[i])
#     if i % 5 == 0:
#         dp[i] = min(dp[i//5]+1, dp[i])
#
# print(dp[x])
#
# # 6분

# # Ch8_DP_개미 전사
#
# x = int(input())
# array = list(map(int, input().split()))
#
# dp = [0] * (x)
# dp[0] = array[0]
# dp[1] = max(array[0], array[1])
#
# for i in range(2, len(array)):
#     dp[i] = max(array[i] + dp[i-2], dp[i-2])
#
# print(dp[x-1])

# 6분