for t in range(int(input())):
    n, m = list(map(int, input().split()))
    temp = list(map(int, input().split()))
    array = [[0] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            array[i][j] = temp[(i * m) + j]

    # dp = [0] * (n * m)
    dp = [[0] * m for i in range(n)]

    for i in range(n):
        # i = 0, 1, 2
        # 필요한 수 = 0, 4, 8
        # column_number = m * i
        #
        # dp[column_number] = array[column_number]
        dp[i][0] = array[i][0]

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

            dp[j][i] = max(left_up, left, left_down) + array[j][i]

        answer = 0

        for j in range(n):
            answer = max(dp[j][i], answer)

    print(answer)


# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2