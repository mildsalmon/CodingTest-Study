"""
Date    : 2021.12.29
Update  : 2021.12.29
Source  : 4485.py
Purpose :
url     : https://www.acmicpc.net/problem/4485
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import heapq

tc = 0

while True:
    n = int(input())

    if n == 0:
        break
    else:
        tc += 1

    graph = []
    for _ in range(n):
        temp = list(map(int, input().split()))

        graph.append(temp)

    dp = [[] for _ in range(n * n)]

        # 오른쪽, 아래, 왼쪽, 위
    ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

    for i in range(n):
        for j in range(n):
            for d in ds:
                dx = i + d[0]
                dy = j + d[1]

                if 0 <= dx < n and 0 <= dy < n:
                    # (비용, x, y)
                    dp[(i*n)+j].append((graph[dx][dy], dx, dy))

    distance = [[1e9] * n for _ in range(n)]
    distance[0][0] = graph[0][0]

    q = []
    heapq.heappush(q, (distance[0][0], 0, 0))

    while q:
        cost, x, y = heapq.heappop(q)

        if distance[x][y] < cost:
            continue

        for next_cost, nx, ny in dp[(x*n)+y]:
            total_cost = cost + next_cost

            if distance[nx][ny] > total_cost:
                distance[nx][ny] = total_cost
                heapq.heappush(q, (total_cost, nx, ny))

    # print(*distance, sep='\n')

    print(f"Problem {tc}: {distance[n-1][n-1]}")