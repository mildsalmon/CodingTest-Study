"""
Date    : 2021.12.29
Update  : 2021.12.29
Source  : 4485.py
Purpose :
url     : https://www.acmicpc.net/problem/4485
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def move(graph, dp, i, j):
    global n

        # 오른쪽, 아래, 왼쪽, 위
    ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

    for d in ds:
        dx = i + d[0]
        dy = j + d[1]

        if 0 <= dx < n and 0 <= dy < n:
            dp[dx][dy] = min(dp[dx][dy], dp[i][j] + graph[dx][dy])

tc = 0

while True:
    n = int(input())

    if n == 0:
        break
    else:
        tc += 1

    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    dp = [[1e9] * n for _ in range(n)]

    dp[0][0] = graph[0][0]

    for i in range(n):
        for j in range(n):
            move(graph, dp, i, j)

    print(*dp, sep='\n')

    print(dp[n-1][n-1])