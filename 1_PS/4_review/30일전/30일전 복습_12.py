# # 바닥공사

# n = int(input())
#
# array = [0] * n
#
# array[0] = 1
# array[1] = 3
#
# for i in range(2, n):
#     array[i] = array[i-2] * 2 + array[i-1]
#
# print(array[-1]%789789)

# 효율적인 화폐 구성
from collections import deque

n, m = list(map(int, input().split()))

coins = []

for i in range(n):
    coins.append(int(input()))

dp = [1e9] * (m+1)
dp[-1] = 0

q = deque()
q.append(m)

while q:
    num = q.popleft()

    for coin in coins:
        if num - coin > 0:
            dp[num - coin] = min(dp[num - coin], dp[num] + 1)
            q.append(num-coin)

print(dp)