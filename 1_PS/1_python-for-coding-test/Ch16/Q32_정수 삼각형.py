n = int(input())

array = [[] for i in range(n)]

for i in range(n):
    temp = list(map(int, input().split()))

    array[i] = temp

dp = [i[:] for i in array]

dp[0] = array[0]

for i in range(1, n):
    for j in range(len(array[i])):
        if len(dp[i-1])-1 < j:
            dp[i][j] = dp[i-1][j-1] + array[i][j]
        elif j-1 < 0:
            dp[i][j] = dp[i-1][j] + array[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + array[i][j]

print(max(dp[-1]))