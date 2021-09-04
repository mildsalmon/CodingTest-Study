# # Ch8_DP_1로 만들기
#
# # 정수 X가 주어질 때, 정수 X에 사용할 수 있는 연산은 4가지다.
#     # X가 5로 나누어떨어지면, 5로 나눈다
#     # X가 3으로 나누어떨어지면, 3으로 나눈다.
#     # X가 2로 나누어떨어지면, 2로 나눈다.
#     # X에서 1을 뺀다.
# # 연산 4개를 수행하여 1을 만들려고 한다.
#
# # 연산을 사용하는 횟수의 최솟값을 출력하라
#
# # Input
#     # 정수 X가 주어진다
#         # 1<= X <= 30,000
# # Output
#     # 연산을 하는 횟수의 최솟값
#
# x = int(input())
# INF = int(1e9)
# dp = [INF] * (x+1)
# dp[0] = 0
# dp[1] = 0
#
# for i in range(2, x+1):
#     dp[i] = dp[i-1]
#     if i % 2 == 0:
#         dp[i] = min(dp[i//2], dp[i])
#     elif i % 3 == 0:
#         dp[i] = min(dp[i//3], dp[i])
#     elif i % 5 == 0:
#         dp[i] = min(dp[i//5], dp[i])
#
#     dp[i] = dp[i] + 1
#
# print(dp[x])

# # 10분 / pass

# ch8_dp_개미 전사

# 메뚜기 식량 창고는 일직선으로 연결되어 있다.
# 각 식량창고에는 정해진 수의 식량을 저장한다.
# 개미 전사는 식량창고를 선택적으로 약탈하여 식량을 빼앗으려고 한다.
# 메뚜기는 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있다.
# 개미 전사가 들키지 않고 식량창고를 약탈해야 한다.

# 식량창고 N개에 대한 정보가 주어졌을 때, 얻을 수 있는 식량의 최댓값을 구하라

# Input
    # 식량창고 개수 N
        # 3 <= N <= 100
    # 식량창고에 저장된 식량의 개수 K
        # 0 <= K <= 1,000

# Output
    # 개미전사가 얻을 수 있는 식량의 최댓값

n = int(input())
array = list(map(int, input().split()))

result = [0] * (n)
result[0] = array[0]
result[1] = array[1]

for i in range(2, n):
    # result[i] = max(result[i] + result[i-2], result[i-1])
    result[i] = max(array[i] + result[i-2], result[i-1])

print(result[-1])

# 13분 5초 / pass