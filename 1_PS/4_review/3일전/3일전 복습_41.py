for t in range(int(input())):
    n, m = list(map(int, input().split()))
    array = list(map(int, input().split()))

    dp = []

    for i in range(n):
        # 0, 1, 2
        dp.append(array[i*m:(i+1)*m])

    for i in range(1, m):
        for j in range(n):
            if j-1 < 0:
                left_up = 0
            else:
                left_up = dp[j-1][i-1]

            if j+1 >= n:
                left_down = 0
            else:
                left_down = dp[j+1][i-1]

            left = dp[j][i-1]

            dp[j][i] = max(left_up, left_down, left) + dp[j][i]

    print(max(list(zip(*dp))[-1]))