"""
Date    : 2022.03.03
Update  : 2022.03.05
Source  : 21923.py
Purpose : dp
url     : https://www.acmicpc.net/problem/21923
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    graph = [list(map(int, input().split())) for _ in range(n)]
    answer = -1e9

    dp_up = [[-1e9] * m for _ in range(n)]
    dp_down = [[-1e9] * m for _ in range(n)]

    dp_up[n-1][0] = graph[n-1][0]

    for r in range(n-1, -1, -1):
        for c in range(m):
            if r == n-1 and c == 0:
                continue

            if r == n-1:
                dp_up[r][c] = max(dp_up[r][c-1] + graph[r][c], dp_up[r][c])
            if c == 0:
                dp_up[r][c] = max(dp_up[r+1][c] + graph[r][c], dp_up[r][c])
            if r != n-1 and c != 0:
                dp_up[r][c] = max(max(dp_up[r][c-1], dp_up[r+1][c]) + graph[r][c], dp_up[r][c])

    # print(*dp_up, sep='\n')

    dp_down[n-1][m-1] = graph[n-1][m-1]

    for r in range(n-1, -1, -1):
        for c in range(m-1, -1, -1):
            if r == n-1 and c == m-1:
                continue

            if r == n-1:
                dp_down[r][c] = max(dp_down[r][c+1] + graph[r][c], dp_down[r][c])
            if c == m-1:
                dp_down[r][c] = max(dp_down[r+1][c] + graph[r][c], dp_down[r][c])
            if r != n-1 and c != m-1:
                dp_down[r][c] = max(max(dp_down[r+1][c], dp_down[r][c+1]) + graph[r][c], dp_down[r][c])

    for r in range(n):
        for c in range(m):
            answer = max(answer, dp_up[r][c] + dp_down[r][c])

    print(answer)