# # 1로 만들기
#
# x = int(input())
# dp = [1e9] * (x+1)
# dp[x] = 0
#
# for i in range(x, 0, -1):
#     if i % 5 == 0:
#         dp[i // 5] = min(dp[i//5], dp[i] + 1)
#     if i % 3 == 0:
#         dp[i // 3] = min(dp[i//3], dp[i] + 1)
#     if i % 2 == 0:
#         dp[i // 2] = min(dp[i//2], dp[i] + 1)
#     dp[i-1] = min(dp[i-1], dp[i] + 1)
#
# print(dp[1])
#
# for i in range(x, 0, -1):
#     div_5 = 1e9
#     div_3 = 1e9
#     div_2 = 1e9
#     minus_1 = 1e9
#
#     if i % 5 == 0:
#         div_5 = dp[i//5]
#         # dp[i // 5] = min(dp[i//5], dp[i] + 1)
#     if i % 3 == 0:
#         div_3 = dp[i//3]
#         # dp[i // 3] = min(dp[i//3], dp[i] + 1)
#     if i % 2 == 0:
#         div_2 = dp[i//2]
#         # dp[i // 2] = min(dp[i//2], dp[i] + 1)
#     # dp[i-1] = min(dp[i-1], dp[i] + 1)
#     minus_1 = dp[i-1]
#
#     dp[i-1] = min(div_5, div_3, div_2, minus_1, dp[i] + 1)
#
# print(dp[1])

# 개미전사

n = int(input())
array = list(map(int, input().split()))

dp = [0] * 101
dp[0] = array[0]
dp[1] = array[1]

for i in range(2, n):
    dp[i] = max(dp[i-2] + array[i], dp[i-1])

print(dp[n-1])