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