# # Ch8_DP_바닥공사
#
# # 가로 길이 N, 세로 길이 2인 직사각형 바닥이 있다.
# # 이 바닥을 1x2, 2x1, 2x2 를 이용해 채우고자 한다.
# # 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성
#
# # Input
#     # N
#         # 1 <= N <= 1,000
#
# # Output
#     # 2xN 바닥을 채우는 방법의 수를 796796으로 나눈 나머지를 출력하라
#
# n = int(input())
#
# a = [0] * 1001
#
# a[1] = 1
# a[2] = 3
#
# for i in range(3, n+1):
#     a[i] = a[i-1] + (2*a[i-2])
#
# print(a[n] % 796796)
#
# # 9분 / 성공

# Ch8_DP_효율적인 화폐 구성

# N종류의 화폐가 있다.
# 화폐들의 개수를 최소한으로 사용해 가치의 합이 M원이 되도록 하라
# 화폐는 개수제한 없이 사용할 수 있다.
# 화폐의 구성은 같지만 순서만 다른 경우는 같은 경우로 구분

# Input
    # N, M
        # 1 <= N <= 100
        # 1 <= M <= 10000
    # N개 줄에 각 화폐의 가치가 주어진다.
        # 화폐의 가치는 10000보다 작거나 같은 자연수

# Output
    # 경우의 수 X
    # 불가능할 경우 -1

n, m = list(map(int, input().split()))
coin = []

for i in range(n):
    coin.append(int(input()))

INF = 1e9

array = [INF] * 10001
max_coin = max(coin)
array[0] = 0

for i in range(max_coin, m+1):
    for j in coin:
        array[i] = min(array[i-j], array[i]) + 1

if array[m] < INF:
    print(array[m])
else:
    print(-1)