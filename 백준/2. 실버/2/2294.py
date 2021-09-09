n, k = list(map(int, input().split()))
array = []
dp = [1e9] * (k+1)

for i in range(n):
    array.append(int(input()))
dp[0] = 0
for coin in array:
    for j in range(coin, k+1):
        dp[j] = min(dp[j], dp[j-coin]+1)

if dp[j] >= 1e9:
    print(-1)
else:
    print(dp[j])