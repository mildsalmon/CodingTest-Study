"""
Date    : 2022.03.03
Update  : 2022.03.03
Source  : 21923.py
Purpose : dp
url     : https://www.acmicpc.net/problem/21923
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    array = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-1e9]*m for _ in range(n)]

    answer = -1e9

    # 상승
    for i in range(n-1, -1, -1):
        for j in range(m):
            if i == n-1 and j == 0:
                temp = array[i][j]
            elif i == n-1:
                temp = array[i][j] + dp[i][j-1]
            elif j == 0:
                temp = array[i][j] + dp[i+1][j]
            else:
                temp = max(dp[i+1][j], dp[i][j-1]) + array[i][j]

            if answer < temp:
                answer = temp
                dp[i][j] = temp
            else:
                j -= 1
                break

    # print(*dp, sep='\n')
    # print(i, j)

    for ii in range(i, n):
        for jj in range(j, m):
            if ii == i and jj == j:
                temp = array[ii][jj] + dp[ii][jj]
            elif ii == i:
                temp = array[ii][jj] + dp[ii][jj-1]
            elif jj == j-1:
                temp = array[ii][jj] + dp[ii-1][jj]
            else:
                temp = max(dp[ii-1][jj], dp[ii][jj-1]) + array[ii][jj]

            dp[ii][jj] = temp

    # print(*dp, sep='\n')

    print(dp[n-1][m-1])
